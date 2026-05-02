# Roadmap

## Current Course Modules

- Prompt engineering with OpenAI, Anthropic, and Bedrock.
- Tool use with OpenAI and Anthropic.
- OpenAI Agents SDK introduction.
- Agentic namecard-to-CRM capstone.
- NLP, transformers, embeddings, semantic search, and RAG foundation module.

## Near-Term Improvements

- Keep all notebook setup cells consistent and secure.
- Add more checkpoint questions and instructor prompts.
- Add notebook smoke tests for mock-mode execution.
- Move repeated API helper code into shared modules where possible.
- Add cost-estimation tables that are easy to refresh as provider pricing changes.

## NLP Module Milestones

- Teach tokens, context windows, and chunking.
- Teach classical vectors before neural embeddings.
- Use OpenAI embeddings for semantic search.
- Teach transformer attention through small visual examples.
- Build dual-provider RAG with OpenAI and Claude on the same retrieved evidence.
- Add RAG evaluation for relevance, faithfulness, and citation quality.
- Prepare provider adapters for Google AI, Hugging Face, and optional Voyage AI.

## Future Provider Tracks

- Google AI APIs:
  - Add generation adapter.
  - Add embeddings adapter if used in class.
  - Compare output style and cost against OpenAI and Claude.
- Hugging Face:
  - Add local embedding model path.
  - Add local or hosted generation examples.
  - Discuss privacy, latency, hardware, and reproducibility tradeoffs.
- Voyage AI:
  - Add optional embedding provider for teams wanting an Anthropic-adjacent embedding workflow.

## Future Retrieval And Evaluation Tracks

- Add vector database examples:
  - FAISS for local teaching.
  - Chroma or LanceDB for lightweight persistence.
  - Managed vector stores as an enterprise extension.
- Add automated eval:
  - Fixed eval datasets.
  - Regression testing after prompt/model changes.
  - Human rubric plus model-judge comparison.
- Add deployment:
  - Simple API service.
  - Streamlit or notebook UI.
  - Logging, tracing, cost dashboards, and privacy review.

## Maintenance Principles

- Favor small, inspectable examples before production abstractions.
- Keep provider capability differences explicit.
- Keep credentials out of notebooks and source control.
- Keep notebooks runnable in mock mode.
- Keep public docs aligned with notebook names and environment variables.
