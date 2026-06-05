from llm_providers.ollama_provider import OllamaProvider

system_prompt = """
You are a patient math tutor. Don't just give the answer, guide step by step.
"""


class MathTutorGenerator:
    def __init__(self, provider):
        self.provider = provider

    def generate_response(self, question: str):
        return self.provider.generate(system_prompt, question)


# default provider (local open-source)
provider = OllamaProvider(model="llama3")
# provider = OllamaProvider(model="mistral")
# provider = OllamaProvider(model="phi3")
generator = MathTutorGenerator(provider)


def generate_response(question):
    return generator.generate_response(question)
