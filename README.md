# Generative AI Course Repository

Course materials for workshops and labs at the Institute of Systems Science (NUS). This repository includes notebooks on prompt engineering, reasoning models, tool use, and agentic AI workflows.

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
pip install anthropic openai boto3 python-dotenv wikipedia tabulate ipython jupyter pandas openai-agents gspread google-auth ipywidgets
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
**Description:** Prompt engineering and model invocation examples using Amazon Bedrock, including multi-model comparisons and Bedrock API usage patterns.

**Dependencies:**
- `boto3` - AWS SDK for Python
- `json` - JSON handling (standard library)

**AWS Configuration:**
- AWS credentials configured via `aws configure` or environment variables
- Access to Amazon Bedrock service

---

#### `prompt_engineering/prompt_engineering_multi_modal_models_amazon_bedrock.ipynb`
**Description:** Multimodal prompt engineering on Amazon Bedrock for image/text scenarios, vision models, and embedding-related workflows.

**Dependencies:**
- `boto3` - AWS SDK for Python
- `json` - JSON handling (standard library)
- `base64` - Base64 encoding/decoding (standard library)

**AWS Configuration:**
- AWS credentials configured via `aws configure` or environment variables
- Access to Amazon Bedrock multimodal models

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

### Uploaded file not recognized
- Re-run the UI cell, then upload again.
- Ensure file is `.jpg`, `.jpeg`, or `.png`.
- Confirm upload status shows filename and byte size.

### Google Sheets write failures
- Verify `GOOGLE_SHEET_ID` and worksheet name.
- Ensure service account has access to the target sheet.
- Ensure sheet header row exactly matches expected CRM columns in the notebook.

## Maintainer Notes

- Keep notebook names stable once labs are published.
- Update this README whenever a lab is renamed or a required env var changes.
