# fortuneteller

# Getting Started

We recommend using the [Anaconda](https://www.anaconda.com/) package manager to avoid dependency/reproducibility problems. For Linux systems, you can find a conda installation guide [here](https://docs.anaconda.com/free/anaconda/install/linux/).

## Installation

1. open your terminal
```bash
2. conda create -n langgraph_env python=3.10 ipython && conda activate langgraph_env && pip install langgraph langchain langchain_openai langchain_community python-dotenv chromadb langchain_chroma gradio
```
3. copy the code from python.py then run

AI Fortune Teller Implementation: "nongpalm หมอลักฟันทิ้ง"
This solution creates a mystical fortune telling experience using modern AI technologies. Here's an overview of the implementation:

Core Technologies
LLM: OpenAI's GPT-4o-mini via langchain_openai.ChatOpenAI
Agentic Framework: LangGraph (from LangChain ecosystem)
Uses StateGraph for conversation flow management
Implements ToolNode for specialized functions
Key Features
Fortune Telling Capabilities
Palm Reading: Analyzes uploaded palm images using GPT-4's vision
Numerology: Calculates life path, expression, soul urge, and personality numbers
Life Guidance: Offers mystical advice for love, career, and wealth
Agent Architecture
Persona: Consistent fortune teller character with mystical language and emojis
Tool Integration: Three specialized tools:
image_analysis_tool: For analyzing palm images
numerology_reading: For processing name and birth date
provide_life_guidance: For area-specific advice
UI Elements (Gradio)
Chat Interface: Conversational experience
Quick Reading Buttons: One-click access to different reading types
Palm Reading Upload: Section for handprint images
Themed Design: Custom CSS for mystical aesthetic
Technical Design Elements
Conversation Memory: ChatHistory class maintains context
Error Handling: Try/except blocks for graceful failure handling
Product Recommendations: Suggests mystical products based on readings
State Management: Tracks conversation flow with LangGraph
Conditional Routing: Logic to determine tool usage or conversation end

