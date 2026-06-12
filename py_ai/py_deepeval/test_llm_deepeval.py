from deepeval import evaluate
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase
from deepeval.test_case import LLMTestCaseParams

test_case = LLMTestCase(
    input="What is the capital of France?",
    actual_output="Paris",
    expected_output="Paris"
)

correctness_metric = GEval(
    name="Correctness",
    criteria="Determine whether the actual output is correct.",
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT
    ],
)

evaluate(
    test_cases=[test_case],
    metrics=[correctness_metric]
)