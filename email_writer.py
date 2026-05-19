import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

st.title("AI Email Writer")
st.subheader("For Marketing Professionals")

business_type = st.text_input("Your Business Type", 
                               placeholder="e.g. Restaurant, Clinic, Shop")
purpose = st.selectbox("Email Purpose", 
                        ["Promotional Offer", "Follow Up", 
                         "Thank You", "New Product Launch"])
tone = st.selectbox("Tone", ["Formal", "Friendly", "Urgent"])

if st.button("Generate Email"):
    model = ChatGroq(model="llama-3.1-8b-instant")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional email writer for businesses."),
        ("user", "Write a {tone} email for a {business_type} business for {purpose}.")
    ])
    chain = prompt | model | StrOutputParser()
    result = chain.invoke({
        "tone": tone,
        "business_type": business_type,
        "purpose": purpose
    })
    st.write(result)