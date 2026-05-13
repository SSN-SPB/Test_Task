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

# Define models to compare
models = [
    {"name": "llama3", "base_url": "http://localhost:11434/v1", "api_key": "ollama"},
    {"name": "mistral", "base_url": "http://localhost:11434/v1", "api_key": "ollama"},
    # {"name": "gpt-4o-mini", "base_url": "https://api.openai.com/v1", "api_key": os.environ["OPENAI_API_KEY"]},
]

# Test questions with expected keywords
test_cases = [
    {
        "question": "What is Langfuse used for?",
        "expected_keywords": ["trace", "monitor", "llm", "observability"],
    },
    {
        "question": "What is Python?",
        "expected_keywords": ["programming", "language"],
    },
    {
        "question": "What is 2 + 2?",
        "expected_keywords": ["4"],
    },
]


def evaluate(question: str, answer: str, expected_keywords: list) -> dict:
    answer_lower = answer.lower()

    # Relevance: does the answer contain expected keywords?
    hits = sum(1 for kw in expected_keywords if kw in answer_lower)
    relevance = hits / len(expected_keywords) if expected_keywords else 0.0

    # Hallucination: answer doesn't contain ANY expected keyword
    hallucination = hits == 0

    # Quality: relevant and not hallucinated
    quality = 1.0 if relevance >= 0.3 and not hallucination else 0.0

    return {
        "quality": quality,
        "hallucination": hallucination,
        "relevance": round(relevance, 2),
    }


for model_config in models:
    client = OpenAI(
        base_url=model_config["base_url"],
        api_key=model_config["api_key"],
    )

    for test in test_cases:
        trace_id = langfuse.create_trace_id()

        with langfuse.start_as_current_observation(
            name=f"compare-{model_config['name']}",
            as_type="generation",
            trace_context={"trace_id": trace_id},
            input={"question": test["question"]},
            metadata={
                "model": model_config["name"],
                "test_case": test["question"],
            },
        ):
            try:
                response = client.chat.completions.create(
                    model=model_config["name"],
                    messages=[{"role": "user", "content": test["question"]}],
                )

                answer = response.choices[0].message.content
                usage = response.usage

                langfuse.update_current_generation(
                    output={"answer": answer},
                    model=model_config["name"],
                    usage_details=(
                        {
                            "input": usage.prompt_tokens or 0,
                            "output": usage.completion_tokens or 0,
                            "total": usage.total_tokens or 0,
                        }
                        if usage
                        else None
                    ),
                )

                observation_id = langfuse.get_current_observation_id()

            except Exception as e:
                answer = f"ERROR: {e}"
                observation_id = langfuse.get_current_observation_id()
                langfuse.update_current_generation(
                    output={"error": str(e)},
                    model=model_config["name"],
                    level="ERROR",
                )

        # Evaluate
        scores = evaluate(test["question"], answer, test["expected_keywords"])

        langfuse.create_score(
            trace_id=trace_id,
            observation_id=observation_id,
            name="quality",
            value=scores["quality"],
            data_type="NUMERIC",
        )

        langfuse.create_score(
            trace_id=trace_id,
            observation_id=observation_id,
            name="hallucination",
            value=scores["hallucination"],
            data_type="BOOLEAN",
        )

        langfuse.create_score(
            trace_id=trace_id,
            observation_id=observation_id,
            name="relevance",
            value=scores["relevance"],
            data_type="NUMERIC",
        )

        print(f"[{model_config['name']}] Q: {test['question']}")
        print(f"  Answer: {answer[:80]}...")
        print(f"  Scores: {scores}")
        print()

langfuse.flush()
print("Done! Check Langfuse dashboard to compare models.")
