# **Generative AI Course Repository**

This repository contains the files and Jupyter notebooks used for teaching courses at the **Institute of Systems Science, National University of Singapore**. The materials focus on prompt engineering, reasoning models, and tool usage with state-of-the-art AI models from OpenAI, Anthropic, and Amazon Bedrock.

---

## **Prerequisites and Setup**

### **Required API Keys and Credentials**

#### **OpenAI API Access**
- **OpenAI API Key**: Required for `prompt_engineering_day1_solution.ipynb`, `prompt_engineering_reasoning_model_day1.ipynb`, and `tooluse_openai.ipynb`.
- Get your API key from: [OpenAI API Keys](https://platform.openai.com/api-keys).
- Set as an environment variable:
  ```bash
  OPENAI_API_KEY=your_openai_api_key
  ```

#### **Anthropic API Access**
- **Anthropic API Key**: Required for `prompt_engineering_day1_solution.ipynb`, `prompt_engineering_anthropic_models_advanced.ipynb`, and `tooluse_anthropic.ipynb`.
- Get your API key from: [Anthropic Console](https://console.anthropic.com/).
- Set as an environment variable:
  ```bash
  ANTHROPIC_API_KEY=your_anthropic_api_key
  ```

#### **Amazon Bedrock Access**
- **AWS Account**: Required for `prompt_engineering_amazon_bedrock.ipynb` and `prompt_engineering_multi_modal_models_amazon_bedrock.ipynb`.
- **AWS IAM Credentials**: Configure AWS CLI with appropriate permissions for Amazon Bedrock.
- **Model Access**: Enable the following models in the Amazon Bedrock Console:
  - Anthropic Claude 3.7 Sonnet
  - Anthropic Claude 3.5 Sonnet
  - Anthropic Claude 3.5 Haiku
  - Amazon Nova Pro
  - Amazon Nova Micro
  - DeepSeek-R1
  - Meta LLama 3.1 70B Instruct

---

### **Models Used in Notebooks**

#### **OpenAI Models**
- **GPT-4o**: Primary model used in `tooluse_openai.ipynb` and `prompt_engineering_reasoning_model_day1.ipynb` (for comparison).
- **GPT-4o-mini**: Fast and cost-effective model used in `prompt_engineering_day1_solution.ipynb`.
- **o3** (`o3-2025-04-16`): Most advanced reasoning model used in `prompt_engineering_reasoning_model_day1.ipynb`.
- **o4-mini** (`o4-mini-2025-04-16`): Cost-effective reasoning model used in `prompt_engineering_reasoning_model_day1.ipynb`.
- **o3-mini** (`o3-mini-2025-01-31`): Balanced reasoning model used in `prompt_engineering_reasoning_model_day1.ipynb`.

#### **Anthropic Models**
- **Claude Opus 4.6** (`claude-opus-4-6`): Most capable model with Extended Thinking feature, used in `prompt_engineering_reasoning_model_day1.ipynb`.
- **Claude Sonnet 4.5** (`claude-sonnet-4-5-20250929`): Balanced model with Extended Thinking, used in `prompt_engineering_reasoning_model_day1.ipynb`.
- **Claude 4.5 Haiku** (`claude-haiku-4-5-20251001`): Fast and cost-effective model used in `prompt_engineering_day1_solution.ipynb`.
- **Claude 3.7 Sonnet**: Used in `tooluse_anthropic.ipynb` and available via Amazon Bedrock.
- **Claude 4.6 Opus** (`claude-opus-4-6`): Used in `prompt_engineering_anthropic_models_advanced.ipynb` for capability comparisons.
- **Claude 4.5 Sonnet** (`claude-sonnet-4-5-20250929`): Used in `prompt_engineering_anthropic_models_advanced.ipynb`.
- **Claude 4.5 Haiku** (`claude-haiku-4-5-20251001`): Primary model used in `prompt_engineering_anthropic_models_advanced.ipynb`.

### **Required Python Libraries**

Install the following packages using `pip`:

```bash
pip install anthropic openai boto3 python-dotenv wikipedia tabulate ipython jupyter
```

---

### **Environment Setup**

1. Create a `.env` file in the root directory with your API keys:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

2. For Amazon Bedrock, configure AWS credentials:
   ```bash
   aws configure
   ```

3. Ensure you have the required permissions for Amazon Bedrock in your AWS account.

## **Jupyter Notebooks Overview**

### **prompt_engineering/prompt_engineering_day1_solution.ipynb**
A comprehensive introduction to prompt engineering for large language models (LLMs) using OpenAI's GPT-4o-mini and Anthropic's Claude Haiku 4.5. Covers principles of prompt design, API usage, message formatting, model parameters (`max_tokens`/`max_completion_tokens`, `temperature`, `stop sequences`), and system prompts. Features both fast and cost-effective models ideal for learning and experimentation. Includes hands-on code examples comparing OpenAI and Anthropic APIs with equivalent model tiers.

### **prompt_engineering/prompt_engineering_anthropic_models_advanced.ipynb**
**The most comprehensive Claude API guide available** - A complete production-ready resource covering everything from basics to advanced patterns.

**Core Fundamentals**: Model selection across Claude 4 family (Opus 4.6, Sonnet 4.5, Haiku 4.5), system prompts for role definition, temperature and parameter tuning (0.0-1.0 ranges with use cases), messages format and conversation history management, few-shot prompting techniques with examples.

**Production Features**: Token counting with cost calculators for all Claude models, robust error handling with exponential backoff retry logic, rate limit management, batch processing with examples, comprehensive best practices checklist (10 categories covering model selection, prompt design, parameters, error handling, cost management, security, testing, production readiness, UX, and maintenance).

**Advanced Capabilities**: Multi-turn conversation management with ConversationManager class, stop sequences for controlled generation, streaming responses for better UX, reusable prompt templates and patterns (PromptTemplate class), JSON mode and structured outputs with parsing helpers, 4 complete real-world use cases (content moderation, document processing, code review, customer support bot).

**Hands-on Examples**: Every concept includes working code examples with output. Advanced use cases demonstrate production-ready patterns combining multiple techniques. Perfect for beginners learning Claude API basics and experienced developers building scalable production applications.

### **prompt_engineering/prompt_engineering_reasoning_model_day1.ipynb**
Comprehensive guide to reasoning models from both OpenAI (o3, o4-mini, o3-mini) and Anthropic (Claude with Extended Thinking). Covers the 4 key principles of prompting reasoning models, cost/performance comparisons, advanced examples (mathematical proofs, code debugging, multi-step planning), and interactive testing functions. Includes detailed model selection guide to help choose the right model for your task. Features enhanced IPython HTML displays, error handling, token usage tracking, and cost analysis for all major reasoning models.

### **prompt_engineering/prompt_engineering_amazon_bedrock.ipynb**
Introduces prompt engineering with Amazon Bedrock's APIs, covering both the basic Invoke API and the more powerful Converse API. Demonstrates text summarization, multi-turn conversations, and function calling capabilities across various foundation models including Claude 3.7 Sonnet, Amazon Nova Pro, and Meta Llama 3.1. Includes practical examples of comparing results across different state-of-the-art models and working with AWS Bedrock's serverless infrastructure.

### **prompt_engineering/prompt_engineering_multi_modal_models_amazon_bedrock.ipynb**
Explores multi-modal capabilities with Amazon Bedrock, including image processing and embeddings. Uses the Titan embedding models to work with product images for similarity search and cross-modal reasoning. The notebook includes practical examples using the product images in the `data/titan-embed/` directory.

### **agents/Lab1_introduction_to_agents_openAI.ipynb**
Provides an introduction to AI agents using OpenAI's Agents SDK. Covers environment setup, API key configuration, and foundational concepts for building agentic applications. Includes detailed setup instructions and troubleshooting guidance for getting started with agent development.

### **tool_use/tooluse_anthropic.ipynb**
Demonstrates how to build and use an agentic tool with Anthropic Claude. The notebook walks through defining a Wikipedia article retrieval tool, setting up a tool schema, and orchestrating a full agentic loop for question answering with external tool calls. It includes practical code for integrating the tool with Claude's API, handling tool use responses, and returning results to the model. Each step is explained with detailed markdown cells for clarity.

### **tool_use/tooluse_openai.ipynb**
Demonstrates how to build and use an agentic tool with OpenAI GPT-4o. The notebook walks through defining a Wikipedia article retrieval tool, setting up a tool schema compatible with OpenAI's function calling API, and orchestrating a full agentic loop for question answering with external tool calls. Features enhanced IPython HTML displays for beautiful, professional presentation of results. Includes practical code for integrating the tool with OpenAI's API, handling tool use responses, and returning results to the model. Each step is explained with detailed markdown cells for clarity.

---

## **Key Features and Updates**

### **Recent Updates (2026-02-08)**
- **Model Updates**:
  - `prompt_engineering_day1_solution.ipynb`: Updated to use fast, cost-effective models (Claude Haiku 4.5 and GPT-4o-mini)
  - `prompt_engineering_reasoning_model_day1.ipynb`: Complete overhaul with latest reasoning models (o3, o4-mini, o3-mini) and Claude Extended Thinking
  - `prompt_engineering_anthropic_models_advanced.ipynb`: **Migrated all Claude 3.x models to Claude 4 family**
    - Updated 6 Claude 3 Opus references → Claude 4.6 Opus (`claude-opus-4-6`)
    - Updated 5 Claude 3.5 Sonnet references → Claude 4.5 Sonnet (`claude-sonnet-4-5-20250929`)
    - Updated 7 Claude 3/3.5 Haiku references → Claude 4.5 Haiku (`claude-haiku-4-5-20251001`)
    - Total: 18 model ID updates ensuring students work with latest, most capable models
- **API Parameter Fix**: Corrected OpenAI API calls to use `max_completion_tokens` instead of deprecated `max_tokens` parameter
- **Bug Fix**: Merged `calculate_cost` function into main setup cell (cell 3) to prevent undefined function errors. The function is now automatically loaded with initial imports and configuration, eliminating the need to manually run additional cells.
- **Major Enhancement: prompt_engineering_anthropic_models_advanced.ipynb** - Transformed into the most comprehensive Claude API guide:
  - **System Prompts**: Complete guide with comparison examples (with/without system prompts), best practices, advanced patterns
  - **Temperature & Parameters**: In-depth coverage with live comparisons across 0.0/0.5/1.0, use case recommendations, top_p and top_k
  - **Token Counting & Cost Management**: Production-ready calculator for Claude 4 family models (Opus 4.6, Sonnet 4.5, Haiku 4.5), real API tracking, cost comparisons
  - **Error Handling & Retry Logic**: Exponential backoff, rate limiting, batch processing with full error taxonomy
  - **Multi-turn Conversations**: ConversationManager class, session management, token tracking, conversation strategies
  - **Stop Sequences**: Controlled generation with delimiters, structured data extraction, dialogue formatting
  - **Streaming Responses**: Real-time output, event handling, token tracking during streams, helper functions
  - **Prompt Templates**: Reusable PromptTemplate class, common patterns library (extraction, classification, analysis, etc.)
  - **JSON Mode & Structured Outputs**: Robust JSON generation, parsing helpers, schema validation, complex nested structures
  - **Advanced Use Cases**: 4 production-ready examples (content moderation, document processing, code review, support bot)
  - **Best Practices Checklist**: 10-category comprehensive guide for production deployment
  - **90 comprehensive cells** covering every concept from fundamentals to advanced use cases
- **New Features in prompt_engineering_reasoning_model_day1.ipynb**:
  - Added all 4 principles for prompting reasoning models (was incomplete)
  - Claude Extended Thinking examples with full integration
  - Cost calculator and performance comparison across models
  - Advanced reasoning examples (math proofs, code debugging, planning)
  - Interactive testing function for custom prompts
  - Comprehensive model selection guide with decision tree
  - Error handling and token usage tracking throughout
  - Enhanced visualizations with IPython HTML displays

### **Enhanced Display System**
- **IPython HTML Integration**: Beautiful, professional HTML displays for AI responses
- **Responsive Design**: Modern styling with gradients, shadows, and typography
- **Tool Use Visualization**: Clear display of tool usage and results
- **Error Handling**: Graceful error display with consistent styling

### **OpenAI API Integration**
- **Function Calling**: Complete implementation of OpenAI's function calling API
- **Tool Schema**: Proper tool schema definition for OpenAI compatibility
- **Message Handling**: Correct message structure for tool calls and responses
- **Error Recovery**: Robust error handling for API interactions

### **Cross-Platform Compatibility**
- **Multiple API Support**: Working examples for OpenAI, Anthropic, and Amazon Bedrock
- **Consistent Interface**: Similar patterns across different API providers
- **Environment Management**: Proper API key and credential handling

### **Data Assets**
- **Product Images**: The `prompt_engineering/data/titan-embed/` directory contains 27 product images used for multi-modal embedding examples
- **Supporting Images**: The `prompt_engineering/images/` directory contains diagrams for temperature and message formatting concepts

---

## **Usage Examples**

### **Basic Tool Use with OpenAI**
```python
from tool_use.tooluse_openai import answer_question

# Ask a question that requires external information
result = answer_question("What is the box office for Nezha 2?")
```

### **Beautiful HTML Display**
```python
from IPython.display import display, HTML

# Display results with professional styling
display_answer_with_html(question, answer)
```

---

## **Contributing**

This repository is maintained for educational purposes at the Institute of Systems Science, National University of Singapore. For questions or issues related to the course materials, please contact the course instructors.

---

## **License**

This repository contains educational materials for the Generative AI course at the Institute of Systems Science, National University of Singapore.