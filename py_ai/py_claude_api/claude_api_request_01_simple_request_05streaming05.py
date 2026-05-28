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

with client.messages.stream(model=model, max_tokens=1000, messages=messages) as stream:
    for text in stream.text_stream:
        # Send each chunk to your client
        # print(text, end="")
        pass

    # Get the complete message for database storage
    final_message = stream.get_final_message()
    print(f"Final message: {final_message.content[0].text}")
