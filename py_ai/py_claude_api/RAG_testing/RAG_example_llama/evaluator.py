import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
EVAL_MODEL = "llama3"


def evaluate_response(question, response, ground_truth):

    eval_prompt = f"""
You are an expert evaluator for math tutoring AI.

QUESTION:
{question}

MODEL RESPONSE:
{response}

GROUND TRUTH:
{ground_truth}

Score each metric from 0 to 1:

1. correctness
2. reasoning_quality
3. instruction_following
4. clarity
5. hallucination

Compute:
overall_score = average of all metrics

Return ONLY valid JSON:
{{
  "correctness": 0,
  "reasoning_quality": 0,
  "instruction_following": 0,
  "clarity": 0,
  "hallucination": 0,
  "overall_score": 0
}}
"""

    payload = {
        "model": EVAL_MODEL,
        "messages": [
            {"role": "system", "content": "You are a strict evaluation system."},
            {"role": "user", "content": eval_prompt},
        ],
        "stream": False,
        "format": "json",
    }

    response = requests.post(OLLAMA_URL, json=payload)

    result_text = response.json()["message"]["content"]

    try:
        return json.loads(result_text)
    except Exception:
        return {"error": "Failed to parse JSON", "raw_output": result_text}
