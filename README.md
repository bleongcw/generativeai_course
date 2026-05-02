# Generative AI Course Repository

Course materials for workshops and labs at the Institute of Systems Science (NUS). The repository teaches practical generative AI through notebooks on prompt engineering, OpenAI and Anthropic APIs, tool use, Amazon Bedrock workflows, agentic AI patterns, and NLP foundations for transformers, embeddings, semantic search, and RAG.

## Repository Structure

- `prompt_engineering/`  
  Prompt engineering, model behavior, reasoning models, and Amazon Bedrock examples.
- `tool_use/`  
  Function and tool-calling workflows with OpenAI and Anthropic.
- `agents/`  
  Agent workflows, orchestration patterns, OpenAI Agents SDK labs, and a namecard-to-CRM capstone.
- `nlp_transformers_embeddings/`  
  New teaching module for tokens, context windows, embeddings, transformer attention, semantic search, dual-provider RAG, evaluation, and future provider adapters.
- `docs/`  
  Architecture notes, roadmap, teaching standards, and extension guidance.

## Recommended Modular Workshop Path

1. `prompt_engineering/prompt_engineering_day1_solution.ipynb`  
   Prompt structure, model parameters, and baseline API usage.
2. `tool_use/tooluse_openai.ipynb` and `tool_use/tooluse_anthropic.ipynb`  
   Tool-calling concepts across provider APIs.
3. `nlp_transformers_embeddings/01_tokens_and_context_windows.ipynb` through `06_rag_evaluation_failure_modes_and_best_practices.ipynb`  
   Foundations from tokens to embeddings, attention, RAG, and evaluation.
4. `agents/Lab1_introduction_to_agents_openAI.ipynb`  
   Agent design, routing, tools, streaming, structured outputs, and production patterns.
5. `agents/Lab2_build_agenticAI_namecard_to_crm.ipynb`  
   Capstone workflow: OCR extraction, research, CRM mapping, and Google Sheets write.
6. Bedrock notebooks in `prompt_engineering/`  
   Optional enterprise/provider-portability extension.

## Quick Setup

### 1. Create and activate a Python environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 2. Install dependencies

For the full repository:

```bash
pip install anthropic openai boto3 python-dotenv wikipedia tabulate ipython jupyter pandas openai-agents gspread google-auth ipywidgets pillow scipy seaborn matplotlib pydantic scikit-learn nbformat nbclient pytest
```

For the new NLP module only:

```bash
pip install -r nlp_transformers_embeddings/requirements.txt
```

### 3. Configure local environment variables securely

Create a local `.env` file in the repository root, or copy `nlp_transformers_embeddings/.env.example` to `nlp_transformers_embeddings/.env`.

Required for OpenAI and Anthropic lessons:

```bash
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
LIVE_API=false
```

Optional for existing and future labs:

```bash
GOOGLE_SERVICE_ACCOUNT_JSON=/absolute/path/to/service_account.json
GOOGLE_SHEET_ID=your_google_sheet_id
GOOGLE_WORKSHEET_NAME=Leads
GOOGLE_API_KEY=your_google_ai_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
VOYAGE_API_KEY=your_voyage_api_key_here
```

Security rules:

- Never commit `.env` files.
- Never paste API keys into notebooks, slides, GitHub, or shared documents.
- Notebooks should show only masked status such as `OPENAI_API_KEY loaded: True`.
- Keep `LIVE_API=false` for offline or demo-safe runs; set it to `true` only when you intentionally want live paid API calls.
- Rotate keys immediately if they are accidentally exposed.

For Bedrock notebooks, configure AWS credentials separately through `aws configure` or environment variables.

## Provider Capability Guide

| Capability | OpenAI | Anthropic Claude | Teaching note |
| --- | --- | --- | --- |
| Text generation | Yes | Yes | Compare style, grounding, refusal behavior, and cost. |
| Structured outputs | Yes | Prompt/schema patterns | Teach reliable output contracts for production. |
| Tool use | Yes | Yes | Keep provider-specific request/response shapes visible. |
| Embeddings | First-party embeddings API | No first-party embeddings API | Use OpenAI embeddings in the core module; mention Voyage AI as an optional Anthropic-documented embedding path. |
| RAG answer synthesis | Yes | Yes | Retrieve once, then compare both answer generators on the same evidence. |
| Evaluation/critique | Yes | Yes | Use both as evaluators, but keep human rubrics and deterministic tests. |

## New NLP, Transformers, Embeddings, And RAG Module

Start at `nlp_transformers_embeddings/README.md`.

Notebook sequence:

1. `01_tokens_and_context_windows.ipynb`
2. `02_embeddings_from_classical_nlp_to_openai.ipynb`
3. `03_attention_and_transformers_visual.ipynb`
4. `04_semantic_search_with_provider_comparison.ipynb`
5. `05_build_a_dual_provider_rag_pipeline.ipynb`
6. `06_rag_evaluation_failure_modes_and_best_practices.ipynb`
7. `07_future_providers_google_huggingface_extension.ipynb`

The module is intentionally markdown-heavy. Each notebook includes learning objectives, concept primers, secure setup, commented code, what-happened explanations, exercises, debugging checklists, production notes, and reflection questions.

## Featured Labs

### Lab 1: OpenAI Agents SDK Introduction

Notebook: `agents/Lab1_introduction_to_agents_openAI.ipynb`

Covers:

- Agent fundamentals
- Function tools and built-in tools
- Handoffs and routing patterns
- Streaming and structured output
- Error handling and cost tracking

### Lab 2: Build Agentic AI Namecard To CRM

Notebook: `agents/Lab2_build_agenticAI_namecard_to_crm.ipynb`

Students learn how to:

1. Extract structured contact data from a namecard image.
2. Run a planner/search/writer deep-research flow with citations.
3. Transform AI outputs into CRM schema fields.
4. Write CRM records to Google Sheets with validation and idempotency checks.

Required environment variables:

- `OPENAI_API_KEY`
- `GOOGLE_SERVICE_ACCOUNT_JSON`
- `GOOGLE_SHEET_ID`
- optional: `GOOGLE_WORKSHEET_NAME` defaults to `Leads`

## Bedrock Model Notes

The Bedrock notebooks use newer model IDs and inference-profile style examples where needed. Current teaching notes include:

- Anthropic examples in Bedrock use `us.` inference-profile style IDs by default.
- The cross-region inference demo uses Amazon Nova Pro for runnable standard-vs-cross-region comparison.
- Some image-generation models may be unavailable depending on account history and Region.
- The multimodal notebook falls back to local placeholder images so embedding and search sections can still run.
- If Bedrock reports that `temperature` and `top_p` cannot both be specified, restart the kernel and rerun the updated notebook cells.

## Documentation

- `docs/architecture.md` explains repository layout, notebook standards, provider adapters, RAG data flow, secret handling, cost strategy, and testing.
- `docs/roadmap.md` tracks current modules, near-term improvements, and future additions such as Google AI, Hugging Face, vector databases, automated evals, and deployment.

## Testing And Smoke Checks

Run deterministic helper checks:

```bash
pytest nlp_transformers_embeddings/tests
```

Import helper modules:

```bash
python -m compileall nlp_transformers_embeddings
```

Notebook guidance:

- All new notebooks run in mock mode without API keys.
- Live OpenAI or Anthropic calls require both a key and `LIVE_API=true`.
- Mock mode is for teaching continuity, not semantic quality benchmarking.

## Troubleshooting

### `ModuleNotFoundError`

- Re-run the install command.
- Restart the kernel.
- Run notebook setup cells from the top.

### API calls do not run

- Confirm the relevant key exists in `.env`.
- Confirm `LIVE_API=true`.
- Confirm you restarted the notebook kernel after editing `.env`.

### Google Sheets write failures

- Verify `GOOGLE_SHEET_ID` and worksheet name.
- Ensure the service account has access to the target sheet.
- Ensure the sheet header row matches the expected CRM columns in the notebook.

### Bedrock model unavailable

- Confirm the model is enabled in your AWS account and Region.
- Use the notebook fallback path if image generation is unavailable.

## Maintainer Notes

- Keep notebook names stable once labs are published.
- Update this README whenever a lab is renamed, an environment variable changes, or model/provider guidance is refreshed.
- Prefer provider adapters and shared helpers over copy-pasting API code across notebooks.
