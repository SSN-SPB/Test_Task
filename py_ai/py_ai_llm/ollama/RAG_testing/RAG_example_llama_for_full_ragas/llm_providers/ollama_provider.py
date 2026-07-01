import requests
from .base import LLMProvider


class OllamaProvider(LLMProvider):
    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/chat"

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
        }

        response = requests.post(self.url, json=payload)
        return response.json()["message"]["content"]