import os
from dotenv import load_dotenv
from langfuse import Langfuse
from openai import OpenAI

load_dotenv()

langfuse = Langfuse(
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    host=os.environ["LANGFUSE_BASE_URL"],
)

# Price per 1M tokens (input/output) — example prices
MODEL_PRICING = {
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "llama3": {"input": 0.00, "output": 0.00},  # free (local)
    "mistral": {"input": 0.00, "output": 0.00},  # free (local)
    # Groq-hosted llama3:
    # "llama3": {"input": 0.05, "output": 0.08},
}


def calculate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Calculate cost in USD for a single request."""
    pricing = MODEL_PRICING.get(model, {"input": 0, "output": 0})
    cost = (input_tokens * pricing["input"] / 1_000_000) + (
        output_tokens * pricing["output"] / 1_000_000
    )
    return round(cost, 6)


def evaluate(answer: str, expected_keywords: list) -> dict:
    answer_lower = answer.lower()
    hits = sum(1 for kw in expected_keywords if kw in answer_lower)
    relevance = hits / len(expected_keywords) if expected_keywords else 0
    hallucination = hits == 0
    quality = 1.0 if relevance >= 0.3 and not hallucination else 0.0
    return {
        "quality": quality,
        "hallucination": hallucination,
        "relevance": round(relevance, 2),
    }


# Models to compare
models = [
    {"name": "llama3", "base_url": "http://localhost:11434/v1", "api_key": "ollama"},
    {"name": "mistral", "base_url": "http://localhost:11434/v1", "api_key": "ollama"},
]

# Test suite
test_cases = [
    {"question": "What is Python?", "expected_keywords": ["programming", "language"]},
    {"question": "What is 2 + 2?", "expected_keywords": ["4"]},
    {
        "question": "Explain machine learning in one sentence.",
        "expected_keywords": ["learn", "data", "algorithm"],
    },
]

# Results
results = []

for model_config in models:
    client = OpenAI(base_url=model_config["base_url"], api_key=model_config["api_key"])

    model_results = {
        "model": model_config["name"],
        "total_cost": 0,
        "avg_quality": 0,
        "scores": [],
    }

    for test in test_cases:
        trace_id = langfuse.create_trace_id()

        with langfuse.start_as_current_observation(
            name=f"cost-compare-{model_config['name']}",
            as_type="generation",
            trace_context={"trace_id": trace_id},
            input={"question": test["question"]},
            metadata={"model": model_config["name"]},
        ):
            response = client.chat.completions.create(
                model=model_config["name"],
                messages=[{"role": "user", "content": test["question"]}],
            )

            answer = response.choices[0].message.content
            usage = response.usage
            input_tokens = usage.prompt_tokens or 0 if usage else 0
            output_tokens = usage.completion_tokens or 0 if usage else 0

            cost = calculate_cost(model_config["name"], input_tokens, output_tokens)

            langfuse.update_current_generation(
                output={"answer": answer},
                model=model_config["name"],
                usage_details={
                    "input": input_tokens,
                    "output": output_tokens,
                    "total": input_tokens + output_tokens,
                },
                cost_details={"total": cost},
            )

            observation_id = langfuse.get_current_observation_id()

        scores = evaluate(answer, test["expected_keywords"])

        langfuse.create_score(
            trace_id=trace_id,
            observation_id=observation_id,
            name="quality",
            value=scores["quality"],
            data_type="NUMERIC",
        )

        model_results["total_cost"] += cost
        model_results["scores"].append(scores["quality"])

    model_results["avg_quality"] = sum(model_results["scores"]) / len(
        model_results["scores"]
    )
    results.append(model_results)

langfuse.flush()

# Print comparison table
print("\n" + "=" * 60)
print(f"{'Model':<12} {'Avg Quality':<14} {'Total Cost':<12} {'Acceptable?'}")
print("=" * 60)

QUALITY_THRESHOLD = 0.8

for r in results:
    acceptable = "✅ YES" if r["avg_quality"] >= QUALITY_THRESHOLD else "❌ NO"
    print(
        f"{r['model']:<12} {r['avg_quality']:<14.2f} ${r['total_cost']:<11.6f} {acceptable}"
    )

print("=" * 60)

# Find cheapest acceptable model
acceptable_models = [r for r in results if r["avg_quality"] >= QUALITY_THRESHOLD]
if acceptable_models:
    best = min(acceptable_models, key=lambda x: x["total_cost"])
    print(
        f"\n🏆 Best value: {best['model']} (quality={best['avg_quality']:.2f}, cost=${best['total_cost']:.6f})"
    )
else:
    print("\n⚠️  No model meets the quality threshold!")
