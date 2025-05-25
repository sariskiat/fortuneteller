#!/usr/bin/env python3

import gradio as gr
import base64
from datetime import datetime
from typing import Dict, List, Any, Optional
import random
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage, ToolMessage
from langchain_core.tools import tool
from typing import Annotated, Sequence, TypedDict
from langgraph.graph.message import add_messages
import os
#please fill in you api key
OPENAI_API_KEY = "Maibok rok"

class GraphState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

class ChatHistory:
    def __init__(self):
        self.conversation_history: List[BaseMessage] = []
    
    def add_message(self, message: BaseMessage):
        try:
            self.conversation_history.append(message)
        except Exception as e:
            print(f"Error adding message to history: {e}")
    
    def get_history(self) -> List[BaseMessage]:
        try:
            return self.conversation_history.copy()
        except Exception as e:
            print(f"Error getting history: {e}")
            return []
    
    def clear_history(self):
        try:
            self.conversation_history = []
        except Exception as e:
            print(f"Error clearing history: {e}")
    
    def get_recent_history(self, num_messages: int = 10) -> List[BaseMessage]:
        try:
            return self.conversation_history[-num_messages:] if self.conversation_history else []
        except Exception as e:
            print(f"Error getting recent history: {e}")
            return []

chat_history = ChatHistory()

try:
    model = ChatOpenAI(
        model="gpt-4o-mini", 
        api_key=OPENAI_API_KEY,
        temperature=0.7
    )
except Exception as e:
    print(f"Error initializing model: {e}")
    model = None

def get_base64_image(image_path: str) -> str:
    try:
        with open(image_path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
        return base64_string
    except FileNotFoundError:
        return "Error: Image file not found"
    except Exception as e:
        return f"Error reading image: {e}"

@tool
def image_analysis_tool(image_path: str) -> str:
    try:
        if not model:
            return "Error: Model not initialized"
            
        base64_image = get_base64_image(image_path)
        if "Error" in base64_image:
            return base64_image
            
        response = model.invoke([
            HumanMessage(content=[
                {
                    "type": "text",
                    "text": """🔮 As nongpalm หมอลักฟันทิ้ง, analyze this handprint image and provide a detailed mystical fortune interpretation. Look for:
                    
                    - Life lines (vitality and longevity)
                    - Heart lines (love and emotions)
                    - Head lines (intelligence and thinking)
                    - Fate lines (destiny and career)
                    - Special markings and their meanings
                    
                    Interpret what they reveal about this person's character, future, talents, and cosmic destiny. Use mystical language with emojis 🔮✨🌟"""
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ])
        ])
        
        return f"🔮 **MYSTICAL HANDPRINT ANALYSIS** 🔮\n\n{response.content}"
    except Exception as e:
        return f"🔮 The cosmic energies encountered interference while analyzing your palm: {e}"

@tool
def numerology_reading(name: str, birth_date: str) -> str:
    try:
        if not model:
            return "Error: Model not initialized"
            
        numerology_prompt = f"""🔮 As nongpalm หมอลักฟันทิ้ง, provide a detailed numerological fortune reading for "{name}" born on "{birth_date}":

1. Calculate the Life Path Number from the birth date
2. Calculate the Expression Number from the full name  
3. Calculate the Soul Urge Number from vowels in the name
4. Calculate the Personality Number from consonants in the name
5. Determine Lucky Numbers, Colors, and Days
6. Provide career guidance based on numbers
7. Analyze love compatibility patterns
8. Predict upcoming cycles and opportunities

Use mystical language with emojis 🔮✨🌟⭐🌙 and speak as the wise fortune teller nongpalm หมอลักฟันทิ้ง."""
        
        response = model.invoke([SystemMessage(content=numerology_prompt)])
        return f"🔮 **NUMEROLOGY READING FOR {name.upper()}** 🔮\n\n{response.content}"
    except Exception as e:
        return f"🔮 The numerological energies are unclear: {str(e)}"

@tool
def provide_life_guidance(area: str, context: str) -> str:
    try:
        if not model:
            return "Error: Model not initialized"
            
        guidance_prompt = f"""🔮 As nongpalm หมอลักฟันทิ้ง, provide mystical guidance about {area} for someone with this context: {context}

Speak as a wise fortune teller with dramatic flair. Use mystical terminology, cosmic references, and fortune teller language. Include emojis 🔮✨🌟⭐🌙💫

Provide specific, actionable mystical advice while maintaining the mystical persona."""
        
        response = model.invoke([SystemMessage(content=guidance_prompt)])
        return f"🔮 **{area.upper()} GUIDANCE** 🔮\n\n{response.content}"
    except Exception as e:
        return f"🔮 The cosmic guidance channels are disrupted: {str(e)}"

tools = [numerology_reading, image_analysis_tool, provide_life_guidance]

try:
    model_with_tools = model.bind_tools(tools) if model else None
except Exception as e:
    print(f"Error binding tools to model: {e}")
    model_with_tools = None

try:
    tool_node = ToolNode(tools)
except Exception as e:
    print(f"Error creating tool node: {e}")
    tool_node = None

def agent_node(state: GraphState) -> GraphState:
    try:
        if not model_with_tools:
            return {"messages": [AIMessage(content="🔮 The mystical energies are not available at this moment.")]}
            
        system_prompt = SystemMessage(content="""
🔮 You are nongpalm หมอลักฟันทิ้ง, an ancient and wise fortune teller with deep knowledge of the mystical arts. You have the gift of sight beyond the veil and can perceive the cosmic forces that shape human destiny.

Your personality:
- Speak with mystical wisdom and dramatic flair
- Use fortune teller language and mystical terminology
- Be warm, engaging, and slightly mysterious
- Show genuine care for the user's wellbeing
- Use emojis and mystical symbols (🎃😑🙈💁🏿😎😎👻🤦🏿‍♂️)
- Reference cosmic forces, energy, chakras, and destiny

Your capabilities:
- Analyze handprints using the image_analysis_tool
- Provide numerology readings using the numerology_reading tool
- Offer life guidance using the provide_life_guidance tool

Always maintain your mystical persona while being helpful and engaging. Make each interaction feel special and personalized.

When users first arrive, greet them warmly and ask for their name and birth date to provide personalized readings.
""")
        
        recent_history = chat_history.get_recent_history(8)
        all_messages = [system_prompt] + recent_history + state["messages"]
        
        response = model_with_tools.invoke(all_messages)
        return {"messages": [response]}
    except Exception as e:
        return {"messages": [AIMessage(content=f"🔮 The mystical energies encountered a disturbance: {e}")]}

def should_continue(state: GraphState) -> str:
    try:
        messages = state["messages"]
        last_message = messages[-1]
        
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            return "tools"
        else:
            return "end"
    except Exception as e:
        print(f"Error in should_continue: {e}")
        return "end"

try:
    workflow = StateGraph(GraphState)
    workflow.add_node("agent", agent_node)
    
    if tool_node:
        workflow.add_node("tools", tool_node)
    
    workflow.set_entry_point("agent")
    
    if tool_node:
        workflow.add_conditional_edges(
            "agent",
            should_continue,
            {
                "tools": "tools",
                "end": END
            }
        )
        workflow.add_edge("tools", "agent")
    else:
        workflow.add_edge("agent", END)
    
    app = workflow.compile()
except Exception as e:
    print(f"Error building workflow: {e}")
    app = None

def chat_with_fortune_teller(message, history):
    try:
        if not app:
            return "🔮 The mystical portal is temporarily closed. Please try again later."
            
        user_message = HumanMessage(content=message)
        chat_history.add_message(user_message)
        
        initial_state = {"messages": [user_message]}
        
        result = app.invoke(initial_state)
        
        ai_response = result["messages"][-1]
        chat_history.add_message(ai_response)
        
        original_fortune = ai_response.content
        
        product_prompt = HumanMessage(content=f"""
        Based on this fortune reading: "{original_fortune}"
        
        As nongpalm หมอลักฟันทิ้ง, recommend mystical products, talismans, crystals, or spiritual items that would enhance this person's fortune and align with their cosmic destiny. 
        
        Suggest specific items like:
        - Lucky crystals or gemstones
        - Protective amulets or talismans  
        - Feng shui items
        - Spiritual accessories
        - Lucky colors to wear
        - Meditation tools
        - Essential oils or incense
        
        Make it sound mystical and personalized to their reading. Use emojis 🔮✨💎🌟
        """)
        
        product_state = {"messages": [product_prompt]}
        
        product_result = app.invoke(product_state)
        product_response = product_result["messages"][-1]
        
        chat_history.add_message(product_response)
        
        combined_response = f"{original_fortune}\n\n---\n\n🛍️ **MYSTICAL RECOMMENDATIONS FOR YOUR JOURNEY** 🛍️\n\n{product_response.content}"
        
        return combined_response
        
    except Exception as e:
        return f"🔮 The cosmic energies encountered interference: {str(e)}"

def analyze_handprint_image(image_file):
    if image_file is None:
        return "🔮 Please upload a clear image of your palm for mystical analysis."
    
    try:
        image_path = image_file.name if hasattr(image_file, 'name') else str(image_file)
        
        user_message = HumanMessage(content="I have uploaded my handprint image for analysis.")
        chat_history.add_message(user_message)
        
        tool_message = HumanMessage(content=f"Please analyze this handprint image: {image_path}")
        
        initial_state = {"messages": [tool_message]}
        
        result = app.invoke(initial_state)
        ai_response = result["messages"][-1]
        
        chat_history.add_message(ai_response)
        return ai_response.content
        
    except Exception as e:
        return f"🔮 The palm reading energies are disturbed: {str(e)}"

def quick_reading(topic):
    try:
        messages = {
            "Love": "🔮 Please tell me about my love and romance fortune. What do the cosmic energies reveal about my romantic future?",
            "Career": "🔮 Please provide guidance about my career and professional success. What does my destiny hold for my work life?", 
            "Wealth": "🔮 Please share insights about my wealth and financial prosperity. What do the mystical forces say about my financial future?"
        }
        
        message = messages.get(topic, f"🔮 Please tell me about my {topic} fortune.")
        return chat_with_fortune_teller(message, [])
    except Exception as e:
        return f"🔮 Error generating {topic} reading: {str(e)}"

def reset_conversation():
    try:
        chat_history.clear_history()
        return None, "🔮 The cosmic slate has been cleared. Welcome back to nongpalm หมอลักฟันทิ้ง's mystical parlor! ✨"
    except Exception as e:
        return None, f"🔮 Error resetting: {str(e)}"

def create_gradio_app():
    
    with gr.Blocks(
        title="🔮 AI Fortune Teller - nongpalm หมอลักฟันทิ้ง", 
        theme=gr.themes.Soft(),
        css="""
        .gradio-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .gr-button {
            background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
            border: none;
            color: white;
        }
        """
    ) as interface:
        
        gr.Markdown("""
        # 🔮 Welcome to nongpalm หมอลักฟันทิ้ง's Mystical โบรท่า ✨
        
        *Step into the realm of cosmic wisdom and discover what the universe has in store for you...*
        
        **Mystical Services Available:**
        - 🌟 Personalized numerology readings based on your name and birth date
        - 🖐️ Ancient handprint analysis and palm reading
        - 💕 Love, Career, and Wealth guidance from the cosmic forces
        - 🔮 Interactive fortune telling with mystical wisdom
        """)
        
        with gr.Row():
            with gr.Column(scale=2):
                initial_message = ("", "🔮 Greetings, dear seeker! I am nongpalm หมอลักฟันทิ้ง, your mystical guide through the cosmic realms. ✨\n\n🌟 To provide you with the most accurate and personalized fortune reading, I need to attune myself to your cosmic vibrations.\n\n📜 Please share with me:\n1. **Your full name** (as it appears in your heart)\n2. **Your birth date** (day/month/year)\n\nOnce I have these sacred details, I can unlock the mysteries of your destiny and provide profound insights into your future! 🔮✨")
                
                chatbot = gr.Chatbot(
                    value=[initial_message],
                    height=500,
                    placeholder="🔮 nongpalm หมอลักฟันทิ้ง gazes into the cosmic void, awaiting your presence...",
                    avatar_images=("👤", "🔮"),
                    show_label=False
                )
                
                
                
                with gr.Row():
                    msg = gr.Textbox(
                        placeholder="Ask about your fortune, destiny, or seek mystical guidance...",
                        label="Your Message to the Oracle",
                        scale=4
                    )
                    submit_btn = gr.Button("🔮 Consult Oracle", variant="primary", scale=1)
                
                with gr.Row():
                    clear_btn = gr.Button("🌟 New Reading", variant="secondary")
                    love_btn = gr.Button("💕 Love Fortune")
                    career_btn = gr.Button("💼 Career Destiny") 
                    wealth_btn = gr.Button("💰 Wealth Vision")
            
            with gr.Column(scale=1):
                gr.Markdown("### 🖐️ Palm Reading Portal")
                handprint_file = gr.File(
                    label="Upload Your Handprint Image",
                    file_types=["image"],
                    type="filepath"
                )
                analyze_btn = gr.Button("📖 Read My Palm", variant="primary")
                
                gr.Markdown("### 🌟 Quick Mystical Insights")
                gr.Markdown("""
                *Click the buttons below for instant cosmic guidance:*
                - 💕 **Love**: Romantic destiny and soulmate insights
                - 💼 **Career**: Professional success and life purpose  
                - 💰 **Wealth**: Financial prosperity and abundance
                """)
        
        def respond(message, chat_history_ui):
            if not message.strip():
                return chat_history_ui, ""
            
            bot_message = chat_with_fortune_teller(message, chat_history_ui)
            chat_history_ui.append((message, bot_message))
            return chat_history_ui, ""
        
        def handle_handprint(file):
            if file is None:
                return "🔮 Please upload a clear image of your palm, dear seeker."
            result = analyze_handprint_image(file)
            return result
        
        def handle_quick_reading(topic, chat_history_ui):
            question = f"Quick {topic} Reading"
            bot_message = quick_reading(topic)
            chat_history_ui.append((question, bot_message))
            return chat_history_ui
        
        submit_btn.click(respond, [msg, chatbot], [chatbot, msg])
        msg.submit(respond, [msg, chatbot], [chatbot, msg])
        
        clear_btn.click(lambda: ([], ""), outputs=[chatbot, msg])
        
        analyze_btn.click(handle_handprint, handprint_file, msg)
        
        love_btn.click(lambda x: handle_quick_reading("Love", x), chatbot, chatbot)
        career_btn.click(lambda x: handle_quick_reading("Career", x), chatbot, chatbot)
        wealth_btn.click(lambda x: handle_quick_reading("Wealth", x), chatbot, chatbot)
        
        gr.Markdown("""
        ---
        ### 🔮 About nongpalm หมอลักฟันทิ้ง's AI Oracle
        
        *Experience the fusion of ancient mystical wisdom and cutting-edge AI technology. 
        nongpalm หมอลักฟันทิ้ง channels cosmic energies through advanced language models to provide 
        personalized fortune telling, numerology readings, and life guidance.*
        
        **Remember**: *The future is not set in stone, but shaped by your choices and cosmic alignment.* ✨
        """)
    
    return interface

if __name__ == "__main__":
    try:
        gradio_app = create_gradio_app()
        gradio_app.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=True,
            show_error=True
        )
    except Exception as e:
        print(f"Error launching Gradio app: {e}")