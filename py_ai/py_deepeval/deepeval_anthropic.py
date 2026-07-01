import os
from dotenv import load_dotenv
from anthropic import Anthropic

from deepeval import evaluate
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams
from deepeval.models.base_model import DeepEvalBaseLLM

load_dotenv()

model_name = "claude-haiku-4-5"
# model_name = "claude-sonnet-4-6"


# -----------------------------
# Claude wrapper (COMPLETE)
# -----------------------------
class ClaudeLLM(DeepEvalBaseLLM):

    def load_model(self):
        # DeepEval expects this to return the "client"
        return Anthropic()

    def get_model_name(self):
        return model_name

    def generate(self, prompt: str) -> str:
        client = self.load_model()
        response = client.messages.create(
            model=model_name,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    async def a_generate(self, prompt: str) -> str:
        client = self.load_model()
        response = client.messages.create(
            model=model_name,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text


llm = ClaudeLLM()


# -----------------------------
# Test case
# -----------------------------
test_case = LLMTestCase(
    input="What is the capital of France?",
    actual_output=llm.generate("What is the capital of France?"),
    expected_output="Paris",
)


# -----------------------------
# GEval (Claude judge)
# -----------------------------
metric = GEval(
    name="Correctness",
    criteria="Check if the answer is factually correct.",
    evaluation_params=[
        SingleTurnParams.INPUT,
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT,
    ],
    model=llm
)


# -----------------------------
# Run evaluation
# -----------------------------
evaluate(
    test_cases=[test_case],
    metrics=[metric],
)