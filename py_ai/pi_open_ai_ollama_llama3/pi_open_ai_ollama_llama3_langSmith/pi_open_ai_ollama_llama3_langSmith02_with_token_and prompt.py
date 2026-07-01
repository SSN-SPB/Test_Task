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
SYSTEM_PROMPT = ("You are a helpful assistant that provides concise answers to questions. "
                 "It is needed only 5 sentences to answer the question. "
                 "Each sentence is maximum 9 words. Numerate sentences. ")
@traceable
def ask_llama(question: str):
    response = client.chat.completions.create(
        model="llama3",
        max_tokens=1000,
        temperature=0.7,
        messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    result = ask_llama("Why is the sky blue?")
    print(result)