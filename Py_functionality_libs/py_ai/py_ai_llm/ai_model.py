from transformers import pipeline

class GenerativeAI:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate_text(self, prompt, max_length=50):
        results = self.generator(prompt, max_length=max_length, num_return_sequences=1)
        print("Generated Text")
        print(results[0]["generated_text"])
        return results[0]["generated_text"]
