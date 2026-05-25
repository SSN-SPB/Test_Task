from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-6"
system_prompts = """You are a Python engineer who writes good and concise code."""
task_message = "Write a Python function that checks a string for duplicate characters."


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
add_user_message(messages, task_message)
simple_answer = chat(messages)
print(f"Only text without system prompt:\n {simple_answer}")

messages = []
add_user_message(messages, task_message)
answer = chat(messages, system=system_prompts)
print(f"Answer with prompt:\n {answer}")
