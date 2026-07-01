from llm_providers.ollama_provider import OllamaProvider
from retriever import SimpleRetriever


# Load document
with open("documents/my_doc.txt", "r") as f:
    text = f.read()


# Simple chunking
documents = [
    text[i:i+200]
    for i in range(0, len(text), 200)
]


retriever = SimpleRetriever(documents)


system_prompt = """
You are a patient and careful assistant.

Guide the user clearly and step by step
when explanations are needed.

Use ONLY the provided context
to answer questions.

Do not invent information.

If the answer is not contained
in the context, say:
"I don't know."
"""


class RAGGenerator:

    def __init__(self, provider):
        self.provider = provider

    def generate_response(self, question):

        context_chunks = retriever.retrieve(question)

        context = "\n".join(context_chunks)

        full_prompt = f"""
Context:
{context}

Question:
{question}
"""

        answer = self.provider.generate(
            system_prompt,
            full_prompt
        )

        return answer, context


provider = OllamaProvider(
    model="llama3"
)

generator = RAGGenerator(provider)


def generate_response(question):
    return generator.generate_response(question)