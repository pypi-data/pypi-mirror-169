import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoConfig, AutoModelForCausalLM, PretrainedConfig, PreTrainedModel
from transformers.modeling_outputs import CausalLMOutput

import warnings



class MultiheadLeap(nn.Module):
    def __init__(self, hidden_size, n_head, window_size, rescale = None, dropout = .1):
        super(MultiheadLeap, self).__init__()
        self.n_head = n_head
        self.hidden_size = hidden_size
        self.head_size = hidden_size // n_head
        self.window_size = window_size
        
        if rescale is not None:
            self.rescale = True
            self.scaling_factor = (1 / self.head_size) * rescale
        else:
            # use normal scaling factor
            self.rescale = False
            self.scaling_factor = (1 / self.head_size**.5)

        self.drop = nn.Dropout(dropout)


    def forward(self, q, f, k, v, attention_mask = None):        
        batch_size, seq_len, hidden_size = v.shape
        
        # reshape for multihead formulation
        q = q.reshape(batch_size, seq_len, self.n_head, self.head_size)
        f = f.reshape(batch_size, seq_len, self.n_head, self.head_size)
        k = k.reshape(batch_size, seq_len, self.n_head, self.head_size)
        v = v.reshape(batch_size, seq_len, self.n_head, self.head_size)
        
        # unparameterized norming of vectors so dot products don't explode (also why it is after reshaping)
        if self.rescale:
            q = self.__real_norm(q)
            f = self.__real_norm(f)
            k = self.__real_norm(k)
            v = self.__real_norm(v)
            
        # dropout regularization (keys don't need dropout as they are always dotted with a dropped out vector)
        q = self.drop(q)
        f = self.drop(f)
        v = self.drop(v)

        # manual "matrix dot product" for speed (in einsum notation "bshe, bshe->bsh") with scaling
        focus_logits = (f * k).sum(dim = -1) * self.scaling_factor
        
        # apply dropout to logits so that all tokens will have a chance at getting focus
        focus_logits = self.drop(focus_logits)
        
        # masking out pad tokens
        if attention_mask is not None:
            focus_logits += attention_mask
        
        # manual softmax within cumulative sum
        focus_weights = torch.exp(focus_logits)
        focus_weights = focus_weights.unsqueeze(-1)
        
        # normalization term for softmax
        cumulative_weights = torch.cumsum(focus_weights, dim = 1)
        cumulative_weights = cumulative_weights - self.__window_align(cumulative_weights)
        
        focused_k = self.__w_focus(focus_weights, cumulative_weights, k)
        focused_v = self.__w_focus(focus_weights, cumulative_weights, v)
        
        # querying by measuring dot product alignment (with scaling)
        alignment = torch.sigmoid((q * focused_k).sum(dim = -1) * self.scaling_factor)
        attention = alignment.unsqueeze(-1) * focused_v
        
        # concat heads
        attention = attention.reshape(batch_size, seq_len, hidden_size)
        
        return attention


    def __real_norm(self, mod):
        # normalize x on the last dimension (the head dimension in this case) with eps term for stability
        return (mod - mod.mean(dim = -1).unsqueeze(-1)) / (mod.std(dim = -1).unsqueeze(-1) + 1e-5)


    def __w_focus(self, focus_weights, cumulative_weights, mod):
        # pass cumulative weights so they don't have to be recalculated
        weighted_mod = torch.cumsum(focus_weights * mod, dim = 1)
        weighted_mod = weighted_mod - self.__window_align(weighted_mod)
        
        # finish softmax by dividing by weight totals (with numerical stability term)
        focused_mod = weighted_mod / (cumulative_weights + 1e-5)
        return focused_mod


    def __window_align(self, mod):
        # zero out the last window_size vectors, and roll these vectors to the front
        # thus, at every sequence index will contain the "past" cumuluative sum to subtract away
        clone_mod = torch.clone(mod) # clone keeps gradients
        clone_mod[:,-self.window_size:] = 0
        clone_mod = torch.roll(clone_mod, self.window_size, dims = 1)
        
        return clone_mod
    
    

class LeapBlock(nn.Module):
    def __init__(self, config, window_size):
        super(LeapBlock, self).__init__()

        self.attn_norm = nn.LayerNorm(config.hidden_size)
        
        # modules for leap
        # note: one large projection matrix is equivalent to having seperate projection matrices and is faster
        self.projections = nn.Linear(config.hidden_size, 4 * config.hidden_size, bias = False)
        self.leap = MultiheadLeap(config.hidden_size, config.n_head, window_size,
                                  rescale = config.rescale, dropout = config.hidden_dropout_prob)

        # modules for feedforward layer (aka boom layer)
        self.boom = nn.Linear(config.hidden_size, config.hidden_size * 4)
        self.activation = nn.GELU()
        self.unboom = nn.Linear(4 * config.hidden_size, config.hidden_size)
        self.boom_norm = nn.LayerNorm(config.hidden_size)
        self.boom_drop = nn.Dropout(config.hidden_dropout_prob)


    def forward(self, mod, attention_mask):
        # pre-norming with projections so each matrix has its own purpose
        q, f, k, v = self.projections(self.attn_norm(mod)).chunk(4, dim = -1)
        
        # unnormed residual connection
        mod = mod + self.leap(q, f, k, v, attention_mask)
        
        # feedforward layer with pre-norming
        mod = mod + self.__boom(self.boom_norm(mod))
        
        return mod


    def __boom(self, mod):
        mod = self.boom(mod)
        mod = self.activation(mod)
        mod = self.unboom(mod)
        
        # possible parameter saving like SHA-RNN (seems to slow down training significantly)
        # mod = torch.stack(mod.chunk(4, dim = -1), dim = -1).sum(dim = -1)
        
        mod = self.boom_drop(mod)

        return mod



class LeapDecoder(nn.Module):
    def __init__(self, config):
        super(LeapDecoder, self).__init__()
        self.config = config
        self.decoders = nn.ModuleList([LeapBlock(config, window_size)
                                       for _, window_size in zip(range(config.n_layer), config.window_sizes)])
        
        self.position_embeddings = nn.Embedding(config.n_positions, config.hidden_size)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)


    def forward(self, input_embs, attention_mask):
        attention_mask = attention_mask.to(dtype = next(self.parameters()).dtype)  # fp16 compatibility
        attention_mask = (1.0 - attention_mask) * -100.0
        attention_mask = attention_mask.unsqueeze(-1)
        
        batch_size, seq_length, _ = input_embs.shape
        position_ids = torch.arange(seq_length, dtype=torch.long, device=input_embs.device)
        position_ids = position_ids.unsqueeze(0).expand(batch_size, -1)
        position_embeddings = self.position_embeddings(position_ids)

        embeddings = input_embs + position_embeddings

        embeddings = self.dropout(embeddings)
        
        layer_outputs = embeddings
        for i, layer_module in enumerate(self.decoders):
            layer_outputs = layer_module(layer_outputs, attention_mask)

        return layer_outputs
    


# Create configuation compatible with HuggingFace
class LeapConfig(PretrainedConfig):
    model_type = "LeapForCausalLM"
    def __init__(self, hidden_size = 256, vocab_size = 32100, n_head = 4,
                 use_local_att = True, window_sizes = None, n_positions = 1024,
                 n_layer = 4, rescale = 10, hidden_dropout_prob = .1,
                 initializer_range = None):
        
        # check head sizes
        assert hidden_size % n_head == 0, "hidden_size is not divisible by n_head"
        
        if (hidden_size // n_head) > 64:
            warnings.warn("Using a hidden_size-to-head ratio of greater than 64 is not ideal as"
                          " LEAP uses a simplified form of attention that relies on having many heads")
        if (hidden_size // n_head) < 32:
            warnings.warn("Using a hidden_size-to-head ratio of less than 64 can sometimes lead to instability")
        
        # check window sizes (and set them automatically if not set)
        assert not (use_local_att is False and window_sizes is not None), \
            "window sizes set when not using local attention"

        if use_local_att is True and window_sizes is not None:
            assert len(window_sizes) == n_layer, "len(window_sizes) should match # of hidden layers"

        elif use_local_att is True and window_sizes is None:
            window_sizes = [n_positions] + [4, 8, 16, n_positions] * (n_layer // 4 + 1)
            
            # first layer should be global attention (to give "context")
            window_sizes[0] = n_positions
            
            # cut down to n_layer
            window_sizes = window_sizes[:n_layer]
        else:
            # don't use windows, i.e. windows are global size
            window_sizes = [n_positions for _ in range(n_layer)]
            
        if initializer_range is None:
            initializer_range = 1 / hidden_size**.5

        super().__init__(
            hidden_size = hidden_size, vocab_size = vocab_size, n_head = n_head,
            use_local_att = use_local_att, window_sizes = window_sizes, n_positions = n_positions,
            n_layer = n_layer, rescale = rescale, hidden_dropout_prob = hidden_dropout_prob,
            initializer_range = initializer_range
        )



class LeapForCausalLM(PreTrainedModel):
    config_class = LeapConfig
    
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.word_embedding = nn.Embedding(config.vocab_size, config.hidden_size)
        self.proj_logits = nn.Linear(config.hidden_size, config.vocab_size, bias = False)
        self.leap_model = LeapDecoder(config)
        self.last_norm = nn.LayerNorm(config.hidden_size)
        self.criterion = nn.CrossEntropyLoss()
        
        # weight tying
        self.proj_logits.weight = self.word_embedding.weight
        
        self.apply(self._init_weights)


    def forward(self, input_ids, attention_mask = None, labels = None, return_dict = False, **kwargs):
        if attention_mask is None:
            attention_mask = torch.ones(input_ids.shape).to(input_ids.device)
        
        embds = self.word_embedding(input_ids)
        layer_outputs = self.leap_model(embds, attention_mask)
        layer_outputs = self.last_norm(layer_outputs)
        logits = self.proj_logits(layer_outputs)
        
        loss = None
        if labels is not None:
            # set pad token labels to -100 to be ignored
            labels.masked_fill_(attention_mask == 0, -100)
            
            # shift logits the same gpt2 does at
            # https://huggingface.co/transformers/v3.5.1/_modules/transformers/modeling_gpt2.html
            shift_logits = logits[..., :-1, :].contiguous()
            shift_labels = labels[..., 1:].contiguous()
            
            loss = self.criterion(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1))
            
        if return_dict is True:
            print("returning")
            return {"loss": loss, "logits": logits}

        return CausalLMOutput(loss = loss, logits = logits)


    def _init_weights(self, module):
        # same initialization as gpt2
        # https://huggingface.co/transformers/v1.1.0/_modules/pytorch_transformers/modeling_gpt2.html
        if isinstance(module, (nn.Linear, nn.Embedding)):
            module.weight.data.normal_(mean = 0.0, std = self.config.initializer_range)
            if isinstance(module, nn.Linear) and module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)



# register config with huggingface
AutoConfig.register("LeapForCausalLM", LeapConfig)
AutoModelForCausalLM.register(LeapConfig, LeapForCausalLM)