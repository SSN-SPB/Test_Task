from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
# model = "claude-haiku-4-5"
model = "claude-sonnet-4-6"


messages = []
messages.append({"role": "user", "content": "What 2*2?"})

response = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
)

print(response.content[0].text)
