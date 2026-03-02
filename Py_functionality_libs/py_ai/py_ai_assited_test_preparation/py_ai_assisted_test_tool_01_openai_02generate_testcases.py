# This code defines a function to generate study flashcards from notes using OpenAI's GPT-4.1-mini model.
# Respose now is: openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details.'. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_cases(requirement: str) -> str:
    prompt = f"""
    You are a QA automation engineer.
    Generate Pytest test cases for the following requirement:

    Requirement:
    {requirement}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content


requirement = "Login should fail if password is incorrect and show an error message"
tests_code = generate_test_cases(requirement)

print(tests_code)