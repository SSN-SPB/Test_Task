from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-6"

# Make a request to the API
message = client.messages.create(
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "How doa I solve 5x+3 =2 for x?"},
    ],
    model=model,
)
print(f"Only text: {message.content[0].text}")
