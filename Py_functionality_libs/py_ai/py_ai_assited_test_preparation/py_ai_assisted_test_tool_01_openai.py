# This code defines a function to generate study flashcards from notes using OpenAI's GPT-4.1-mini model.
# Respose now is: openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details.'. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_flashcards(notes, n=5):
    prompt = f"""
Create {n} high-quality study flashcards from the notes below.
Return JSON in this format:
[
  {{"question": "...", "answer": "..."}},
  ...
]

Notes:
{notes}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful exam-prep tutor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content
    return json.loads(content)

# Example usage
notes = """
Neural networks are computational models inspired by the human brain.
They consist of layers of neurons that learn representations of data.
Backpropagation is used to train neural networks by minimizing error.
"""

cards = generate_ai_flashcards(notes)

for c in cards:
    print("Q:", c["question"])
    print("A:", c["answer"])
    print()