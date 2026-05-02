# Architecture

## Repository Layout

The course is organized by learning theme:

- `prompt_engineering/`: foundational and advanced prompt engineering, reasoning models, and Bedrock.
- `tool_use/`: OpenAI and Anthropic tool-use patterns.
- `agents/`: agent workflows and applied capstone labs.
- `nlp_transformers_embeddings/`: tokens, embeddings, transformers, semantic search, RAG, evaluation, and future provider adapters.
- `docs/`: maintainers' architecture and roadmap notes.

## Notebook Teaching Standard

Every new teaching notebook should include:

- Learning objectives
- Concept primer
- Secure setup cell
- Markdown before every major code block
- Code comments that explain intent, data flow, and provider-specific behavior
- "What just happened?" explanation after important output
- Student exercise
- Debugging checklist
- Production best practices
- Reflection questions

This makes the notebooks usable both in instructor-led workshops and self-paced learning.

## Provider Adapter Pattern

The NLP module separates capabilities from provider names:

- `EmbeddingProvider`: converts text to vectors.
- `GenerationProvider`: produces language-model responses.
- `EvaluationProvider`: scores answers or critiques grounding.

Current implementation:

- OpenAI: embeddings, generation, structured output, RAG answers, evaluation.
- Anthropic Claude: generation, query rewriting, synthesis, critique, evaluation.
- Future: Google AI, Hugging Face, and optional Voyage AI adapters.

This pattern prevents provider-specific code from spreading through every notebook.

## RAG Data Flow

The RAG notebooks follow this data flow:

1. Load source documents.
2. Split documents into chunks with source metadata.
3. Embed chunks.
4. Embed or rewrite the user query.
5. Rank chunks by cosine similarity.
6. Assemble a grounded prompt with passage IDs.
7. Generate an answer with OpenAI and/or Claude.
8. Evaluate relevance, faithfulness, and citation quality.

The core helper modules are:

- `nlp_transformers_embeddings/utils/retrieval.py`
- `nlp_transformers_embeddings/utils/openai_client.py`
- `nlp_transformers_embeddings/utils/anthropic_client.py`
- `nlp_transformers_embeddings/utils/schemas.py`
- `nlp_transformers_embeddings/utils/viz.py`
- `nlp_transformers_embeddings/utils/mock_data.py`

## Secret Handling

API keys are loaded from `.env` files and never printed. Notebooks show only whether a key is loaded.

Required live keys:

```bash
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

Optional future keys:

```bash
GOOGLE_API_KEY=your_google_ai_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
VOYAGE_API_KEY=your_voyage_api_key_here
```

Security defaults:

- `.env` and `*.env` are ignored.
- `.env.example` is committed as a template.
- `LIVE_API=false` keeps notebooks in mock mode.
- Live calls require both a key and `LIVE_API=true`.

## Cost And Retry Strategy

Teaching notebooks should:

- Use mock mode by default.
- Make live API calls only when explicitly enabled.
- Keep prompts short and inspectable.
- Explain which stage costs money: embedding, generation, search, or evaluation.
- Add retries only in applied labs where temporary failure would disrupt class flow.

Production-oriented labs should also track latency, input tokens, output tokens, model name, provider, and estimated cost.

## Testing And Mock Mode

Deterministic tests cover:

- Chunking
- Cosine similarity
- Retrieval ranking shape
- Schema validation

Run:

```bash
pytest nlp_transformers_embeddings/tests
python -m compileall nlp_transformers_embeddings
```

Mock mode is a teaching tool. It verifies pipeline shape and classroom continuity, but not production semantic quality.
