import os
from dotenv import load_dotenv
from anthropic import Anthropic

from deepeval import evaluate
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams
from deepeval.models.base_model import DeepEvalBaseLLM

load_dotenv()

# -----------------------------
# MODEL CONFIG
# -----------------------------
TESTED_MODEL = "claude-haiku-4-5"        # system you are testing
JUDGE_MODEL = "claude-sonnet-4-6"        # evaluator (better reasoning)


# -----------------------------
# ANTHROPIC CLIENT
# -----------------------------
client = Anthropic()
# client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# -----------------------------
# WRAPPER FOR ANY CLAUDE MODEL
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
# 1. TESTED MODEL (SYSTEM UNDER TEST)
# -----------------------------
tested_llm = ClaudeLLM(TESTED_MODEL)

# -----------------------------
# 2. JUDGE MODEL (EVALUATOR)
# -----------------------------
judge_llm = ClaudeLLM(JUDGE_MODEL)


# -----------------------------
# TEST CASE (run tested model here)
# -----------------------------
test_input = "What is the capital of France?"

test_case = LLMTestCase(
    input=test_input,
    actual_output=tested_llm.generate(test_input),
    expected_output="Paris",
)


# -----------------------------
# METRIC (uses judge model)
# -----------------------------
metric = GEval(
    name="Correctness",
    criteria="Check if the answer is factually correct and matches expected output.",
    evaluation_params=[
        SingleTurnParams.INPUT,
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT,
    ],
    model=judge_llm   # 🔥 IMPORTANT: evaluation model
)


# -----------------------------
# RUN EVALUATION
# -----------------------------
evaluate(
    test_cases=[test_case],
    metrics=[metric],
)