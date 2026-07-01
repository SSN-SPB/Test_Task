from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-6"
tested_message = "Write one sentence about fake database."


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


messages = []
add_user_message(messages, tested_message)

stream = client.messages.create(
    model=model, max_tokens=1000, messages=messages, stream=True
)

for event in stream:
    print(event)
