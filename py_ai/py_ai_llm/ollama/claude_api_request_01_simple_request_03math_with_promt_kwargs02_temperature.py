from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-6"
system_prompts = """You are a patient math tutor. Don't just give the answer a student's questions, but guide them to solution step by step."""


def chat(messages, system=None, temperature=0.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }

    if system:
        params["system"] = system_prompts

    message = client.messages.create(**params)
    return message.content[0].text

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

messages = []
add_user_message(messages, "Add one sentence movie plot.")
simple_answer = chat(messages, temperature=0.0)
print(f"Temperature 0:\n {simple_answer}")

messages = []
add_user_message(messages, "Add one sentence movie plot.")
answer = chat(messages, temperature=0.7)
print(f"Temperature 1: \n {answer}")
