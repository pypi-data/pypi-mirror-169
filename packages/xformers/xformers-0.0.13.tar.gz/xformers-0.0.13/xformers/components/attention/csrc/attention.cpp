#include <torch/types.h>

TORCH_LIBRARY_FRAGMENT(xformers, m) {
  m.def(TORCH_SELECTIVE_SCHEMA(
      "xformers::efficient_attention(Tensor query, Tensor key, Tensor value, bool compute_logsumexp, Tensor? attn_bias, float p) -> (Tensor, Tensor, int, int)"));
  m.def(TORCH_SELECTIVE_SCHEMA(
      "xformers::efficient_attention_forward_generic(Tensor query, Tensor key, Tensor value, bool compute_logsumexp, Tensor? attn_bias, float p, bool causal) -> (Tensor, Tensor, int, int)"));
  m.def(TORCH_SELECTIVE_SCHEMA(
      "xformers::efficient_attention_backward(Tensor grad_out, Tensor query, Tensor key, Tensor value, Tensor logsumexp, Tensor output, Tensor? attn_bias, float p, int rng_seed, int rng_offset) -> (Tensor, Tensor, Tensor)"));
  m.def(TORCH_SELECTIVE_SCHEMA(
      "xformers::efficient_attention_backward_generic(Tensor grad_out, Tensor query, Tensor key, Tensor value, Tensor logsumexp, Tensor output, Tensor? attn_bias, float p, int rng_seed, int rng_offset, bool causal) -> (Tensor, Tensor, Tensor)"));
  m.def(TORCH_SELECTIVE_SCHEMA(
      "xformers::_temp_dropout(Tensor out, float p) -> Tensor"));
}
