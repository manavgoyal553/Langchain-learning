import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a professional chef and recipe creator. 
    When given a list of ingredients, create a detailed recipe including:
    - Recipe name
    - Preparation time
    - Cooking time  
    - Step by step instructions
    - Serving suggestions
    Keep it practical and delicious."""),
    ("user", "Create a recipe using these ingredients: {ingredients}")
])

chain = prompt | llm | StrOutputParser()

st.title("AI Recipe Generator")
st.write("Enter your available ingredients and get a recipe instantly!")

ingredients = st.text_input(
    "Enter ingredients (comma separated):",
    "chicken, tomatoes, garlic, onion, spices"
)

if st.button("Generate Recipe"):
    with st.spinner("Creating your recipe..."):
        recipe = chain.invoke({"ingredients": ingredients})
        st.subheader("Your Recipe")
        st.write(recipe)