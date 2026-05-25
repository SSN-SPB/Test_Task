from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-0"

# Make a request to the API
message = client.messages.create(
    max_tokens=1000,
    messages=[{"role": "user", "content": "Write a haiku about the ocean in russian."}],
    model=model,
)
print(f"Only text: {message.content[0].text}")
