import requests
import json


OLLAMA_URL = "http://localhost:11434/api/chat"

EVAL_MODEL = "llama3"


def evaluate_response(question, answer, context, ground_truth):

    eval_prompt = f"""
You are an expert evaluator for RAG systems.

QUESTION:
{question}

RETRIEVED CONTEXT:
{context}

MODEL ANSWER:
{answer}

GROUND TRUTH:
{ground_truth}

Evaluate from 0 to 1:

1. correctness
2. faithfulness
   (Is answer supported by context?)

3. context_relevance
   (Was retrieved context useful?)

4. hallucination
   (Did model invent information?)

Compute:
overall_score = average of all metrics

Return ONLY JSON:

{{
  "correctness": 0,
  "faithfulness": 0,
  "context_relevance": 0,
  "hallucination": 0,
  "overall_score": 0
}}
"""

    payload = {
        "model": EVAL_MODEL,
        "messages": [
            {"role": "system", "content": "You are a strict evaluator."},
            {"role": "user", "content": eval_prompt},
        ],
        "stream": False,
        "format": "json",
    }

    response = requests.post(OLLAMA_URL, json=payload)

    result = response.json()

    print("\nEVALUATOR RAW RESPONSE:")
    print(result)

    try:
        return json.loads(result["message"]["content"])

    except Exception:

        return {"error": "Failed to parse JSON", "raw_output": result}
