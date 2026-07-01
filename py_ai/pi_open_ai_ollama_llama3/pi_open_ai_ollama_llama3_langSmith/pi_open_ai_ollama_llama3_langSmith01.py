from openai import OpenAI
from langsmith.wrappers import wrap_openai
from langsmith import traceable

# OpenAI-compatible Ollama endpoint
client = wrap_openai(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required but unused
    )
)

@traceable
def ask_llama(question: str):
    response = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "user", "content": question}
        ],
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    result = ask_llama("Why is the sky blue?")
    print(result)