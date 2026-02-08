# **Generative AI Course Repository**

This repository contains the files and Jupyter notebooks used for teaching courses at the **Institute of Systems Science, National University of Singapore**. The materials focus on prompt engineering, reasoning models, and tool usage with state-of-the-art AI models from OpenAI, Anthropic, and Amazon Bedrock.

---

## **Prerequisites and Setup**

### **Required API Keys and Credentials**

#### **OpenAI API Access**
- **OpenAI API Key**: Required for `prompt_engineering_day1_solution.ipynb`, `reasoning_openAI.ipynb`, and `tooluse_openai.ipynb`.
- Get your API key from: [OpenAI API Keys](https://platform.openai.com/api-keys).
- Set as an environment variable:
  ```bash
  OPENAI_API_KEY=your_openai_api_key
  ```

#### **Anthropic API Access**
- **Anthropic API Key**: Required for `prompt_engineering_day1_solution.ipynb`, `understanding_anthropic_models.ipynb`, and `tooluse_anthropic.ipynb`.
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
- **GPT-4o**: Primary model used in `tooluse_openai.ipynb` and `reasoning_openAI.ipynb`.
- **GPT-5.2**: Used in `prompt_engineering_day1_solution.ipynb`. OpenAI's flagship model for coding and agentic tasks.
- **GPT-4 Turbo**: Used in `reasoning_openAI.ipynb`.
- **o3**: Advanced reasoning model used in `reasoning_openAI.ipynb`.

#### **Anthropic Models**
- **Claude 3.7 Sonnet**: Used in `tooluse_anthropic.ipynb` and available via Amazon Bedrock.
- **Claude 3.5 Haiku**: Used in `understanding_anthropic_models.ipynb`.
- **Claude Sonnet 4.5**: Used in `prompt_engineering_day1_solution.ipynb`. Anthropic's most intelligent model for coding and complex agents.
- **Claude 3 Haiku**: Used in `understanding_anthropic_models.ipynb`.

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
A comprehensive introduction to prompt engineering for large language models (LLMs) such as OpenAI's GPT-5.2 and Anthropic's Claude Sonnet 4.5. Covers principles of prompt design, API usage, message formatting, model parameters (`max_tokens`, `temperature`, `stop sequences`), and system prompts. Includes hands-on code examples for both OpenAI and Anthropic APIs.

### **prompt_engineering/understanding_anthropic_models.ipynb**
Demonstrates how to retrieve and display a list of available models from the Anthropic AI platform using their Python client. Includes code for listing models, formatting output, and optional enhanced display with the `tabulate` library.

### **prompt_engineering/reasoning_openAI.ipynb**
Focuses on advanced prompting and reasoning with OpenAI's latest models (including `o1` and GPT-4 series). Shows how to list available OpenAI models, construct effective reasoning prompts, and use structured formats. Includes practical code for generating functions and outputs using reasoning models. Features enhanced IPython HTML displays for better visualization of results.

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