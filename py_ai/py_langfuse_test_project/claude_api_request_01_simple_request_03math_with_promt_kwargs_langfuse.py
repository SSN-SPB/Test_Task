from dotenv import load_dotenv
from anthropic import Anthropic
from langfuse import Langfuse
import os
langfuse = Langfuse()
load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-6"
# model = "claude-haiku-4-5"
system_prompts = """You are a patient math tutor. Don't just give the answer a student's questions, but guide them to solution step by step."""
load_dotenv()

# Debug check
print("Anthropic key loaded:", os.getenv("ANTHROPIC_API_KEY") is not None)


def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system_prompts

    message = client.messages.create(**params)
    return message.content[0].text

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

messages = []
add_user_message(messages, "How do a I solve 5x+3 =2 for x?")
simple_answer = chat(messages)
print(f"Only text without system prompt:\n {simple_answer}")

messages = []
add_user_message(messages, "How do a I solve 5x+3 =2 for x?")
answer = chat(messages, system=system_prompts)
print(f"Answer with prompt:\n {answer}")



langfuse.flush()