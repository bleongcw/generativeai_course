# Generative AI Course Repository

Course materials for workshops and labs at the Institute of Systems Science (NUS). This repository includes notebooks on prompt engineering, reasoning models, tool use, Amazon Bedrock workflows, and agentic AI patterns.

## Repository Structure

- `prompt_engineering/`:
  Prompt engineering, model behavior, and reasoning examples.
- `agents/`:
  Agent workflows, orchestration patterns, and hands-on labs.
- `tool_use/`:
  Function/tool-calling workflows with OpenAI and Anthropic.

## Quick Setup

### 1) Python dependencies

```bash
pip install anthropic openai boto3 python-dotenv wikipedia tabulate ipython jupyter pandas openai-agents gspread google-auth ipywidgets pillow scipy seaborn matplotlib
```

### 2) Environment variables

Create a `.env` file in `/Users/bernardleong/Workspaces/nus-iss/generativeai_course`:

```bash
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_SERVICE_ACCOUNT_JSON=/absolute/path/to/service_account.json
GOOGLE_SHEET_ID=your_google_sheet_id
GOOGLE_WORKSHEET_NAME=Leads
```

Notes:
- `GOOGLE_SERVICE_ACCOUNT_JSON` can be either a JSON file path or raw JSON string.
- For Bedrock notebooks, configure AWS credentials separately via `aws configure`.

## Bedrock Model Updates

The Bedrock notebooks in this repository were refreshed to align with newer Bedrock model availability and lifecycle constraints.

### Current model mapping used in this course

- `Claude 3.7 Sonnet` -> `Claude Sonnet 4.5` using `us.anthropic.claude-sonnet-4-5-20250929-v1:0`
- `Claude 3.5 Haiku` -> `Claude Haiku 4.5` using `us.anthropic.claude-haiku-4-5-20251001-v1:0`
- `Meta Llama 3.1 70B Instruct` -> `Meta Llama 4 Maverick 17B Instruct` using `us.meta.llama4-maverick-17b-instruct-v1:0`
- Multimodal image generation examples were updated from Titan Image Generator to Nova Canvas defaults
- Titan Multimodal Embeddings remain in place for the image-text embedding workflow

### Important Bedrock notes

- Anthropic examples in this course use `us.` inference-profile style IDs by default.
- The cross-region inference demo in the Bedrock notebook uses `Amazon Nova Pro` for the runnable standard-vs-cross-region comparison, because newer Anthropic models may not support plain on-demand model IDs in all accounts.
- Some Bedrock image models may be marked legacy or unavailable depending on your account history and Region. The multimodal notebook now falls back to locally generated placeholder images so the embedding and semantic-search sections can still run.
- If your account has a different active image-generation model, update the helper `model_id` in the multimodal notebook before running the image generation section.

## Featured Labs

### Lab 1: OpenAI Agents SDK Introduction

Notebook:
- `/Users/bernardleong/Workspaces/nus-iss/generativeai_course/agents/Lab1_introduction_to_agents_openAI.ipynb`

Covers:
- agent fundamentals
- function tools and built-in tools
- handoffs and routing patterns
- streaming and structured output
- error handling and cost tracking

### Lab 2: Build Agentic AI Namecard to CRM

Notebook:
- `/Users/bernardleong/Workspaces/nus-iss/generativeai_course/agents/Lab2_build_agenticAI_namecard_to_crm.ipynb`

#### Learning objectives
Students will learn how to:
1. Extract structured contact data from a namecard image.
2. Run a planner/search/writer deep-research flow with citations.
3. Transform AI outputs into CRM schema fields.
4. Write CRM records to Google Sheets with validation and idempotency checks.

#### Lab 2 flow
1. Stage 1: OCR and namecard extraction.
2. Stage 2: Deep research on person and company.
3. Stage 3: CRM mapping and Google Sheets write.

#### Lab 2 requirements
- `OPENAI_API_KEY`
- `GOOGLE_SERVICE_ACCOUNT_JSON`
- `GOOGLE_SHEET_ID`
- optional: `GOOGLE_WORKSHEET_NAME` (default: `Leads`)

#### Lab 2 run instructions
1. Open the notebook and run cells from top to bottom.
2. Use **Upload Namecard** to upload a JPG/PNG.
3. Confirm uploaded filename appears in the UI.
4. Optionally correct extracted fields manually.
5. Click **Run Pipeline**.
6. Review Stage 1/2/3 outputs and final sheet write status.

#### Lab 2 guardrails implemented
- schema validation with Pydantic
- confidence scoring and low-confidence warnings
- fallback behavior when live API calls fail
- Google Sheets header validation
- duplicate guard using `(email, company)`

## Notebook Catalog

### Agents

#### `agents/Lab1_introduction_to_agents_openAI.ipynb`
**Description:** Comprehensive introduction to OpenAI Agents SDK covering agent fundamentals, tools (function and built-in), handoffs and routing patterns, streaming, structured outputs, error handling, and cost tracking.

**Dependencies:**
- `openai` - OpenAI Python client
- `pandas` - Data manipulation and analysis
- `python-dotenv` - Environment variable management

**Environment Variables:**
- `OPENAI_API_KEY` (required)

---

#### `agents/Lab2_build_agenticAI_namecard_to_crm.ipynb`
**Description:** End-to-end agentic AI workflow that extracts contact information from namecard images, conducts deep research on the person and company, and writes structured CRM records to Google Sheets with validation and idempotency checks.

**Dependencies:**
- `openai` - OpenAI Python client
- `pydantic` - Data validation and schema modeling
- `pandas` - Data manipulation
- `gspread` - Google Sheets API client
- `google-auth` - Google authentication
- `ipywidgets` - Interactive UI widgets for Jupyter
- `python-dotenv` - Environment variable management

**Environment Variables:**
- `OPENAI_API_KEY` (required)
- `GOOGLE_SERVICE_ACCOUNT_JSON` (required) - Path to service account JSON or raw JSON string
- `GOOGLE_SHEET_ID` (required)
- `GOOGLE_WORKSHEET_NAME` (optional, default: "Leads")

---

### Prompt Engineering

#### `prompt_engineering/prompt_engineering_day1_solution.ipynb`
**Description:** Foundational prompt design exercises across OpenAI and Anthropic providers. Covers prompt structure, instruction clarity, parameter tuning, and baseline prompt patterns.

**Dependencies:**
- `openai` - OpenAI Python client
- `anthropic` - Anthropic Python client
- `python-dotenv` - Environment variable management

**Environment Variables:**
- `OPENAI_API_KEY` (required)
- `ANTHROPIC_API_KEY` (required)

---

#### `prompt_engineering/prompt_engineering_reasoning_model_day1.ipynb`
**Description:** Reasoning-model focused exercises comparing advanced reasoning workflows, step-wise problem solving, deeper analysis prompts, and model-behavior tradeoffs.

**Dependencies:**
- `openai` - OpenAI Python client
- `anthropic` - Anthropic Python client
- `python-dotenv` - Environment variable management
- `ipython` - Enhanced interactive Python shell
- `jupyter` - Jupyter notebook environment

**Environment Variables:**
- `OPENAI_API_KEY` (required)
- `ANTHROPIC_API_KEY` (required)

---

#### `prompt_engineering/prompt_engineering_anthropic_models_advanced.ipynb`
**Description:** Advanced Anthropic-focused prompt engineering covering model selection, robust prompting patterns, production-oriented practices, and Claude-specific features.

**Dependencies:**
- `anthropic` - Anthropic Python client

**Environment Variables:**
- `ANTHROPIC_API_KEY` (required)

---

#### `prompt_engineering/prompt_engineering_amazon_bedrock.ipynb`
**Description:** Prompt engineering and model invocation examples using Amazon Bedrock, including Claude Sonnet 4.5, Claude Haiku 4.5, Amazon Nova models, DeepSeek-R1, and Meta Llama 4 Maverick 17B Instruct. Covers `InvokeModel`, `Converse`, cross-region inference, streaming, code generation, and function calling.

**Dependencies:**
- `boto3` - AWS SDK for Python
- `json` - JSON handling (standard library)

**AWS Configuration:**
- AWS credentials configured via `aws configure` or environment variables
- Access to Amazon Bedrock service
- Access to the Bedrock models enabled in your account

**Notes:**
- Anthropic examples use `us.` inference-profile IDs by default.
- The notebook includes a built-in `get_weather()` fallback so the function-calling section does not depend on manual copy-paste.
- Bedrock parameter settings were updated to avoid newer Claude validation conflicts such as sending both `temperature` and `top_p`.

---

#### `prompt_engineering/prompt_engineering_multi_modal_models_amazon_bedrock.ipynb`
**Description:** Multimodal prompt engineering on Amazon Bedrock for image/text scenarios, image generation, and embedding-based semantic search. The notebook now defaults to Nova Canvas-style image generation while keeping Titan Multimodal Embeddings for the shared vector-space workflow.

**Dependencies:**
- `boto3` - AWS SDK for Python
- `json` - JSON handling (standard library)
- `base64` - Base64 encoding/decoding (standard library)
- `pillow` - Image handling
- `numpy` - Numerical operations
- `scipy` - Distance calculations for search
- `seaborn` / `matplotlib` - Similarity heatmap visualization

**AWS Configuration:**
- AWS credentials configured via `aws configure` or environment variables
- Access to Amazon Bedrock multimodal models

**Notes:**
- If no active Bedrock image-generation model is available in your account, the notebook automatically creates local placeholder product images so the later embedding and search sections can still run.
- If `PIL` import fails, install Pillow with `python -m pip install pillow`.

---

### Tool Use

#### `tool_use/tooluse_openai.ipynb`
**Description:** OpenAI function-calling and tool-use patterns demonstrating tool integration, conversational tool use, parallel tool calls, and safe response parsing.

**Dependencies:**
- `openai` - OpenAI Python client
- `python-dotenv` - Environment variable management

**Environment Variables:**
- `OPENAI_API_KEY` (required)

---

#### `tool_use/tooluse_anthropic.ipynb`
**Description:** Anthropic tool-use patterns demonstrating tool definition, invocation flow, response handling, and practical integration patterns with Claude.

**Dependencies:**
- `anthropic` - Anthropic Python client

**Environment Variables:**
- `ANTHROPIC_API_KEY` (required)

## Troubleshooting

### `ModuleNotFoundError` (e.g., `gspread`)
- Re-run setup/import cells.
- Restart kernel and run from top.

### `ModuleNotFoundError: No module named 'PIL'`
- Install Pillow with `python -m pip install pillow`.
- Restart the kernel after installation.

### Uploaded file not recognized
- Re-run the UI cell, then upload again.
- Ensure file is `.jpg`, `.jpeg`, or `.png`.
- Confirm upload status shows filename and byte size.

### Google Sheets write failures
- Verify `GOOGLE_SHEET_ID` and worksheet name.
- Ensure service account has access to the target sheet.
- Ensure sheet header row exactly matches expected CRM columns in the notebook.

### Bedrock `ValidationException` for Claude parameters
- If Bedrock reports that `temperature` and `top_p` cannot both be specified, restart the kernel and rerun the updated notebook cells.
- The current course notebooks are written to use only one of those sampling controls per Claude request.

### Bedrock image model marked legacy or unavailable
- Some Amazon image models may be unavailable in a given account even if they appear in Bedrock listings.
- The multimodal notebook now falls back to local placeholder images so the rest of the lab can continue.
- If you have another active image-generation model in your Bedrock account, update the helper `model_id` before rerunning the image generation section.

## Maintainer Notes

- Keep notebook names stable once labs are published.
- Update this README whenever a lab is renamed, a required env var changes, or the Bedrock model lineup for the course is refreshed.
