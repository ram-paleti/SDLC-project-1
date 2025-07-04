import streamlit as st
from api_client import generate_code

st.set_page_config(page_title="SmartSDLC", layout="wide")

st.title("🚀 SmartSDLC – AI-Powered Code Generator")

prompt = st.text_area("Enter your requirement or prompt", height=200)

if st.button("Generate Code"):
    if prompt.strip():
        with st.spinner("Generating code using AI..."):
            result = generate_code(prompt)
            st.subheader("🧠 AI-Generated Code:")
            st.code(result, language="python")
    else:
        st.warning("⚠️ Please enter a prompt.")
