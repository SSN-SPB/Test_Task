from anthropic import Anthropic
from dotenv import load_dotenv
import json

load_dotenv()
client = Anthropic()

model = "claude-sonnet-4-6"


def evaluate_response(question, response, ground_truth):
    eval_prompt = f"""
You are an expert evaluator for math tutoring AI.

TASK:
Evaluate the model response based on correctness and reasoning quality.

QUESTION:
{question}

MODEL RESPONSE:
{response}

GROUND TRUTH ANSWER:
{ground_truth}

Score each metric from 0 to 1:

1. correctness
2. reasoning_quality
3. instruction_following
4. clarity
5. hallucination (1 = no hallucination, 0 = hallucinated steps)

Return ONLY valid JSON:
{{
  "correctness": ,
  "reasoning_quality": ,
  "instruction_following": ,
  "clarity": ,
  "hallucination": ,
  "overall_score":
}}
"""

    message = client.messages.create(
        model=model,
        max_tokens=800,
        messages=[{"role": "user", "content": eval_prompt}],
    )

    return message.content[0].text
