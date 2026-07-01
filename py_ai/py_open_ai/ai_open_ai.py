import openai
import time


class GenerativeAI:
    def __init__(self, model="gpt-4"):
        self.model = model

    def generate_text(self, prompt, max_tokens=50):
        """Generates text using OpenAI API."""
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
        )
        end_time = time.time()

        generated_text = response["choices"][0]["message"]["content"]
        response_time = end_time - start_time  # Calculate response time

        return generated_text, response_time
