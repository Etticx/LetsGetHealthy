# app.py
import streamlit as st
from knowledge_base import questions
from inference_engine import run_inference

# Page Setup
st.set_page_config(page_title="ISP543 MadMuscles Clone", layout="wide")

st.title("💪 ISP543: Fitness Expert System")
st.markdown("**Logic:** Rule-Based Forward Chaining with Constraints")
st.markdown("---")

# 1. SIDEBAR - GENERATE 7 INPUTS
st.sidebar.header("User Profile")
st.sidebar.markdown("*Answer the 7 questions:*")

user_inputs = {}

# Loop through the questions dictionary
for key, q_data in questions.items():
    user_inputs[key] = st.sidebar.selectbox(q_data["text"], q_data["options"])

# 2. MAIN AREA
if st.sidebar.button("Generate My Plan"):
    
    # Run the Engine
    result = run_inference(user_inputs)
    
    st.success("✅ Expert Plan Generated Successfully")
    
    # 3 Column Layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🏋️ Strategy & Exercises")
        st.info(result["strategy"]) 
        # Note: The 'Finisher' exercise will appear here automatically!
        
    with col2:
        st.subheader("🗓 Schedule")
        st.warning(result["schedule"])
        
    with col3:
        st.subheader("🎒 Equipment")
        st.error(result["equipment"])

else:
    st.info("👈 Please configure the **7 Inputs** on the sidebar.")
