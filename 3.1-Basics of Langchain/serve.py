from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model=ChatGroq(model="llama-3.1-8b-instant")

## Prompt Template
generic_template="translate the following into {language}:"

prompt=ChatPromptTemplate.from_messages(
    [("system",generic_template),("user","{text}")]
)

parser=StrOutputParser()

## Create Chain
chain=prompt|model|parser

## App definition

app=FastAPI(title="langchain server",
            version="1.0",
            description="A simple API server using langchain runnable interfaces")

## Adding chain route
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)