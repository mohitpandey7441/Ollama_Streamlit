import streamlit as st
from ollama import Client 

# ✅ Create client instance (VERY IMPORTANT)
client = Client(host="http://localhost:11434") 

st.set_page_config(
    page_title="Custom LLM model by Prakash Senapati - Ollama",
    layout="centered"
)

st.title("Mr. Mohit Pandey - Ollama App")

prompt = st.text_area("Enter your prompt:", height=200)

if st.button("Generate Response"):
    if prompt.strip() == "gemma4:31b-cloud":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(
                model="gemma4:31b-cloud",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.success("Response Generated!")
            st.write(response["message"]["content"])


