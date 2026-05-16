import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

## prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistent. Please answer tot he question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain demo with Gemma model")
input_text=st.text_input("What question you have in mind?")

## Ollama Gemma model
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))