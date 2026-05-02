# NLP, Transformers, Embeddings, And RAG

This module teaches NLP foundations from basic to advanced through a practical path:

tokens -> context windows -> classical vectors -> OpenAI embeddings -> transformer attention -> semantic search -> dual-provider RAG -> evaluation.

The module uses both OpenAI and Anthropic throughout the learning journey. OpenAI is used for first-party embeddings and generation. Anthropic Claude is used for generation, query rewriting, critique, synthesis, and evaluation. This distinction is intentional: students should learn provider capabilities honestly instead of assuming every model API exposes the same primitives.

## Environment Setup

Install dependencies:

```bash
pip install -r nlp_transformers_embeddings/requirements.txt
```

Create a local `.env` file by copying `.env.example`:

```bash
cp nlp_transformers_embeddings/.env.example nlp_transformers_embeddings/.env
```

Required keys for live provider comparisons:

```bash
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

Optional future-provider keys:

```bash
GOOGLE_API_KEY=your_google_ai_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
VOYAGE_API_KEY=your_voyage_api_key_here
```

Use mock mode by default:

```bash
LIVE_API=false
```

Set `LIVE_API=true` only when you intentionally want live paid API calls.

## Security Rules For Students

- Treat API keys like passwords.
- Never hard-code keys in notebooks.
- Never print full keys.
- Never commit `.env`.
- Never upload `.env` to GitHub or shared classroom systems.
- Use output such as `OPENAI_API_KEY loaded: True`, not the key value.
- Rotate any key that was accidentally exposed.

## Notebook Sequence

1. `01_tokens_and_context_windows.ipynb`  
   Tokens, context windows, provider message shapes, and chunking intuition.
2. `02_embeddings_from_classical_nlp_to_openai.ipynb`  
   Bag-of-words, cosine similarity, OpenAI embeddings, and semantic retrieval.
3. `03_attention_and_transformers_visual.ipynb`  
   Q/K/V, attention weights, positional signals, and contextual representations.
4. `04_semantic_search_with_provider_comparison.ipynb`  
   OpenAI embedding retrieval with OpenAI and Claude query/explanation comparison.
5. `05_build_a_dual_provider_rag_pipeline.ipynb`  
   One retrieval layer, two generation providers, grounded answers, and citations.
6. `06_rag_evaluation_failure_modes_and_best_practices.ipynb`  
   Retrieval relevance, faithfulness, citation quality, and common RAG failures.
7. `07_future_providers_google_huggingface_extension.ipynb`  
   Adapter stubs for Google AI, Hugging Face, and optional Voyage embeddings.

## Teaching Standard

Each notebook includes:

- Learning objectives
- Concept primer
- Provider comparison notes
- Markdown before code
- Code comments explaining intent and data flow
- "What just happened?" sections
- Student exercises
- Debugging checklist
- Production best practices
- Reflection questions

## Important Provider Note

Anthropic does not currently provide a first-party embeddings API. This module therefore uses OpenAI embeddings for the core vector path and uses Claude for language-model tasks around retrieval: query rewriting, answer synthesis, critique, and evaluation. Anthropic documentation points to external providers such as Voyage AI when embeddings are needed; Voyage support is prepared as an optional future adapter, not required for this module.

## Mock Mode

All notebooks run without API keys using deterministic mock behavior. Mock mode is designed for classroom continuity and pipeline comprehension. It should not be used to benchmark semantic retrieval quality or provider quality.

## Local Tests

```bash
pytest nlp_transformers_embeddings/tests
python -m compileall nlp_transformers_embeddings
```
