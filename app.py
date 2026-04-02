import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import pandas as pd
import os

# --- 🖥️ Page Configuration ---
st.set_page_config(page_title="Lore-Master OS | Gamyopedia", page_icon="🕹️", layout="wide")

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=1500,   
    temperature=0.7,
    do_sample=True
)

model=ChatHuggingFace(llm=llm)

# --- 🛰️ Header Section ---
st.title("📟 LORE-MASTER OS: LEGACY EDITION")
st.markdown("### *💠 📜 History is written by the players. We just archive it 💠*")
st.subheader("Want to refresh storylines? Lets go!!")
st.divider()

# --- 💾 Load Dataset ---
@st.cache_data
def load_data():
    return pd.read_csv("data/games.csv")

df = load_data()

# --- 🛠️ Sidebar: The "Hardware Settings" ---
with st.sidebar:
    st.header("⚙️ SYSTEM CONFIG")
    
    style = st.selectbox(
        "🎙️ Narrator Voice-Pack",
        ["Gritty Veteran 🎖️", "Sarcastic Robot 🤖", "Professional Historian 📜", 
         "Excited Fanboy 🤩", "Conspiracy Theorist 🕵️‍♂️", "Film Noir Detective 🕵️",
         "Grandmother 👵", "RPG Quest Giver 🛡️", "Sports Commentator 🎙️"]
    )
    
    depth = st.select_slider(
        "🌫️ Fog of War (Lore Depth)",
        options=["The Vibe Check 💨", "Quick Recap ⏱️", "Standard ⚖️", "Deep Lore 📚", "The Completionist 🏆"],
        value="Standard ⚖️",
        help="Clear the Fog of War to reveal more hidden map data."
    )
    
    spoilers = st.radio("🛡️ Anti-Cheat (Spoiler Shield)", ["Strictly No Spoilers 🔒", "Minor Hints 🔑", "Full Spoilers! 💣"], horizontal=True)
    
    st.divider()
    st.info("⚠️ **Nerf Warning:** Higher detail settings may consume more Mana (API tokens).")

# --- 🕹️ Main Layout ---
col1, col2 = st.columns([2, 1])

with col1:
    with st.container(border=True):
        option = st.selectbox(
            "💾 INSERT CARTRIDGE (Select Game):",
            df['name'],
            placeholder="🔍 Searching memory card...",
            accept_new_options=True
        )
        
        focus = st.pills(
            "🎯 SKILL TREE FOCUS (Target Systems):",
            ["Main Plot ⚔️", "Character Backstory 👤", "World Building 🌍", 
             "Hidden Secrets 🕵️‍♀️", "Tactical Context 🧠", "Philosophical Themes 🧘", "Community Myths 👻"],
            selection_mode="multi",
            default=["Main Plot ⚔️"]
        )

with col2:
    with st.container(border=True):
        format_type = st.segmented_control(
            "📤 SAVE FILE FORMAT",
            options=["Story 📖", "Bullet Points 📝", "Radio Log 📻", "Poem 📜"],
            default="Story 📖"
        )
        
        st.write("") # Spacer
        # The main Action Button
        generate_btn = st.button("🎮 PRESS START / EXECUTE", use_container_width=True, type="primary")

# --- 🧠 Generation Logic ---
if generate_btn:
    if not focus:
        st.warning("🚨 **GLITCH DETECTED:** You must select at least one Skill Tree focus!")
    else:
        with st.status("📡 ESTABLISHING PING...", expanded=True) as status:
            st.write(f"🧬 Loading Voice-Pack Asset: {style}...")
            
            try:
                focus_str = ", ".join(focus)
                
                depth_map = {
                    "The Vibe Check 💨": "Write in 100 words only.",
                    "Quick Recap ⏱️": "Write in 100-300 words.",
                    "Standard ⚖️": "Write in around 300-500 words.",
                    "Deep Lore 📚": "Write in 500-700 words with detailed explanations.",
                    "The Completionist 🏆": "Write in 700+ words with maximum depth, including hidden details, subplots, and analysis."
                }


                template = load_prompt("Template.json") 
                prompt = template.invoke({
                    'format_type': format_type,
                    'spoilers': spoilers,
                    'focus': focus_str, 
                    'depth': depth_map.get(depth),
                    'style': style,
                    'option': option
                })
                ori_prompt=prompt
                text_output=""
                st.write("🔓 Achievement Unlocked: Accessing Hidden Files...")
                for _ in range(0,10):
                    response = model.invoke(prompt)
                    text = response.content.strip()
                    
                    text_output = text_output+text + "\n"
                    
                    # stop if complete sentence
                    if text.endswith(('.', '!', '?')):
                        break
                    
                    # continue from where it stopped
                    prompt = text + "\nContinue the story seamlessly keeping the same tone and everything same"
                status.update(label="✅ LEVEL CLEAR: DATA SYNCED", state="complete", expanded=True)
                
                # --- 🎬 Result Display ---
                st.markdown("---")
                st.subheader(f"📟 BOSS LOOT: {option.upper()} 💎")
                
                with st.container(border=True):
                    st.markdown(text_output)
                
                st.toast("🏆 GG! Lore successfully decrypted!", icon="⭐")
                st.snow() # Using snow for a "cool" effect
                
            except Exception as e:
                status.update(label="💀 BLUE SCREEN OF DEATH (BSOD)", state="error")
                st.error(f"🚫 **SYSTEM CRASH:** Connection to the server timed out. \n\n`Crash Log: {e}`")
                st.button("🔄 Respawn (Retry)")