from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-6"
system_promts = """You are a patient math tutor. Don't just give the answer a student's questions, but guide them to solution step by step."""

# Make a request to the API
message = client.messages.create(
    system=system_promts,
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "How do a I solve 5x+3 =2 for x?"},
    ],
    model=model,
)
print(f"Only text: {message.content[0].text}")
