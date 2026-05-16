import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

st.title("Multi-Model Comparator")
st.write("Compare responses from different AI models on the same prompt")

prompt_text = st.text_input("Enter your prompt:", "What is generative AI?")

if prompt_text:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Answer concisely in 3-4 sentences."),
        ("user", "{question}")
    ])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Groq (llama-3.1-8b)")
        with st.spinner("Groq thinking..."):
            groq_llm = ChatGroq(model="llama-3.1-8b-instant")
            groq_chain = prompt | groq_llm | StrOutputParser()
            groq_response = groq_chain.invoke({"question": prompt_text})
            st.write(groq_response)

    with col2:
        st.subheader("Ollama (gemma:2b)")
        with st.spinner("Ollama thinking..."):
            ollama_llm = Ollama(model="gemma:2b")
            ollama_chain = prompt | ollama_llm | StrOutputParser()
            ollama_response = ollama_chain.invoke({"question": prompt_text})
            st.write(ollama_response)