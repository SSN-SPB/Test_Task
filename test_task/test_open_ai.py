import openai
from openai import OpenAI

openai.api_key = "EMPTY"
api_base = "https://mixtral-api.llm.lab.epam.com/v1"
client = OpenAI(api_key="EMPTY", base_url=api_base)
print(client.models.list())
model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
# normal completion
completion = client.completions.create(
    model=model, prompt="Hi who are you?", max_tokens=100
)

# chat completion
completion = client.chat.completions.create(
    model=model,
    # messages
    messages=[{"role": "user", "content": "Please provide explanation for asteroids"}],
    # model parameters
    max_tokens=None,
)

# chat completion with assistant and user (example of history usage)
completion = client.chat.completions.create(
    model=model,
    # messages
    messages=[
        {
            "role": "user",
            "content": "You are a gourmet who has seen numerous countries. Please use your experiences to guide others.",
        },
        {"role": "assistant", "content": "How can I guide you?"},
    ],
    # model parameters
    max_tokens=None,
)
