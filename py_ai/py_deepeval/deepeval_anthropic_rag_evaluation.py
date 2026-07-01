import os
from dotenv import load_dotenv
from anthropic import Anthropic

from deepeval import evaluate
from deepeval.metrics import GEval, FaithfulnessMetric, ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase, SingleTurnParams
from deepeval.models.base_model import DeepEvalBaseLLM

load_dotenv()

# -----------------------------
# MODELS
# -----------------------------
GENERATOR_MODEL = "claude-haiku-4-5"
JUDGE_MODEL = "claude-sonnet-4-6"

client = Anthropic()
# client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# -----------------------------
# CLAUDE WRAPPER
# -----------------------------
class ClaudeLLM(DeepEvalBaseLLM):

    def __init__(self, model_name: str):
        self.model_name = model_name

    def load_model(self):
        return client

    def get_model_name(self):
        return self.model_name

    def generate(self, prompt: str) -> str:
        response = client.messages.create(
            model=self.model_name,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    async def a_generate(self, prompt: str) -> str:
        response = client.messages.create(
            model=self.model_name,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text


# -----------------------------
# MODELS INIT
# -----------------------------
generator_llm = ClaudeLLM(GENERATOR_MODEL)
judge_llm = ClaudeLLM(JUDGE_MODEL)


# -----------------------------
# SIMPLE RAG RETRIEVER (mock)
# Replace this with FAISS / Pinecone / Elastic in real system
# -----------------------------
def retrieve_context(query: str):
    return [
        "Paris is the capital and largest city of France.",
        "France is located in Western Europe.",
        "Paris is known for the Eiffel Tower."
    ]


# -----------------------------
# RAG PIPELINE (generator)
# -----------------------------
def rag_pipeline(query: str):
    context = retrieve_context(query)

    prompt = f"""
Answer the question using ONLY the context below.

Context:
{chr(10).join(context)}

Question:
{query}
"""

    answer = generator_llm.generate(prompt)

    return context, answer


# -----------------------------
# RUN RAG SYSTEM
# -----------------------------
query = "What is the capital of France?"

context, answer = rag_pipeline(query)


# -----------------------------
# TEST CASE (RAG-aware)
# -----------------------------
test_case = LLMTestCase(
    input=query,
    actual_output=answer,
    expected_output="Paris",
    retrieval_context=context  # 🔥 KEY FOR RAG EVALUATION
)


# -----------------------------
# METRICS
# -----------------------------

# 1. Correctness (judge = Claude Sonnet)
correctness = GEval(
    name="Answer Correctness",
    criteria="Check if the answer correctly answers the question using context.",
    evaluation_params=[
        SingleTurnParams.INPUT,
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT,
    ],
    model=judge_llm
)


# 2. Faithfulness (hallucination detection)
faithfulness = FaithfulnessMetric(
    model=judge_llm
)

# 3. Context relevance (retrieval quality)
context_relevance = ContextualRelevancyMetric(
    model=judge_llm
)


# -----------------------------
# EVALUATE
# -----------------------------
evaluate(
    test_cases=[test_case],
    metrics=[
        correctness,
        faithfulness,
        context_relevance
    ],
)