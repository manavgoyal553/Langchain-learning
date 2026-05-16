import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is LangChain and why is it useful?"}
    ]
)

print(message.content[0].text)