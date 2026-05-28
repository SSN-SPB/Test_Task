from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

model = "claude-sonnet-4-6"

system_prompt = """
You are a patient math tutor. Don't just give the answer to a student's question, but guide them step by step.
"""


def generate_response(question):
    message = client.messages.create(
        system=system_prompt,
        max_tokens=1000,
        messages=[{"role": "user", "content": question}],
        model=model,
    )
    return message.content[0].text
