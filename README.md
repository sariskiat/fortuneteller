# fortuneteller

# Getting Started

We recommend using the [Anaconda](https://www.anaconda.com/) package manager to avoid dependency/reproducibility problems. For Linux systems, you can find a conda installation guide [here](https://docs.anaconda.com/free/anaconda/install/linux/).

## Installation

1. open your terminal
```bash
2. conda create -n langgraph_env python=3.10 ipython && conda activate langgraph_env && pip install langgraph langchain langchain_openai langchain_community python-dotenv chromadb langchain_chroma gradio
```
3. copy the code from python.py please fill in your api key <img width="406" alt="image" src="https://github.com/user-attachments/assets/42fd78d0-0a3b-4c3f-888c-1adb34f8940a" />
then run

# 🔮 AI Fortune Teller Implementation: "nongpalm หมอลักฟันทิ้ง"

This solution creates a **mystical fortune telling experience** using modern AI technologies. Below is an overview of its implementation, architecture, and features.

---

## 🌐 Core Technologies

- **LLM**: OpenAI's `gpt-4o-mini` via `langchain_openai.ChatOpenAI`
- **Agentic Framework**: [LangGraph](https://docs.langchain.com/langgraph/)
  - Utilizes `StateGraph` for managing structured conversation flow
  - Implements `ToolNode` for specialized tasks and dynamic routing

---

## 🔑 Key Features

### 🖐️ Fortune Telling Capabilities

- **Palm Reading**  
  Analyzes uploaded handprint images using GPT-4o’s vision capabilities to deliver palmistry-based insights.

- **Numerology**  
  Calculates mystical values including:
  - Life Path Number
  - Expression Number
  - Soul Urge Number
  - Personality Number

- **Life Guidance**  
  Offers fortune-teller-style advice on:
  - 💖 Love
  - 💼 Career
  - 💰 Wealth

---

## 🧠 Agent Architecture

- **Persona**:  
  A consistent fortune teller identity, speaking with mystical flair and emoji-laced responses.

- **Tool Integration**  
  Uses three specialized tools:
  - `image_analysis_tool`: Interprets uploaded palm images.
  - `numerology_reading`: Analyzes names and birthdates for numerology profiles.
  - `provide_life_guidance`: Responds to user queries in themed categories.

---

## 💻 UI Elements (Gradio)

- **Chat Interface**:  
  Seamless conversational flow with the AI fortune teller.

- **Quick Reading Buttons**:  
  Pre-set options for immediate insights (e.g., "Numerology", "Love Advice").

- **Palm Reading Upload**:  
  File uploader for hand images.

- **Themed Design**:  
  Custom CSS for a mystical and engaging aesthetic.

---

## ⚙️ Technical Design Elements

- **Conversation Memory**  
  `ChatHistory` class stores prior user inputs to ensure contextual continuity.

- **Error Handling**  
  Graceful fallback using `try/except` blocks for unpredictable inputs or tool failures.

- **Product Recommendations**  
  Suggests lucky colors, accessories, or CJ More’s items aligned with the user’s fortune.

- **State Management**  
  LangGraph tracks conversation states, routes based on user input and intent detection.

- **Conditional Routing**  
  Determines which tool to invoke (or when to end chat) based on detected intent.

---
## ✨ Challenges Faced

- I had never used LangGraph before, so I had to watch many tutorials to understand how it works.
- Initially, I tried to make the graph too complicated by combining results and invoking tools again. I solved this by starting fresh and keeping the design simple—within the limits of what I could manage.
- The model initially told me it couldn't read the image input directly. However, the real issue was that I wasn’t calling the tools correctly. It took me some time to debug and understand how tool invocation works and trace whether the tools were actually being called.




---
