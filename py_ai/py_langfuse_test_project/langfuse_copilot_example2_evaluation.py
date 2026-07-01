import os

from dotenv import load_dotenv
from langfuse import Langfuse

load_dotenv()

langfuse = Langfuse(
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    host=os.environ["LANGFUSE_BASE_URL"],
)


def evaluate_answer(user_question: str, answer: str) -> dict:
    answer_lower = answer.lower()
    question_words = set(user_question.lower().split())

    overlap = sum(1 for w in question_words if w in answer_lower)
    relevance = min(1.0, overlap / max(1, len(question_words)))

    hallucination = "guaranteed fact" in answer_lower or "100% certain" in answer_lower
    quality = 1.0 if relevance >= 0.3 and not hallucination else 0.0

    return {
        "quality": quality,
        "hallucination": hallucination,
        "relevance": round(relevance, 2),
    }


user_question = "What is Langfuse used for?"
model_answer = (
    "Langfuse is used to trace, monitor, and evaluate LLM applications. "
    "It helps track inputs, outputs, scores, latency, and quality."
)

trace_id = langfuse.create_trace_id()
observation_id = None

with langfuse.start_as_current_observation(
    name="qa-example",
    as_type="generation",
    trace_context={"trace_id": trace_id},
    input={"question": user_question},
):
    langfuse.update_current_generation(
        output={"answer": model_answer},
        model="demo-model2",
        usage_details={
            "input": 12,
            "output": 18,
            "total": 30,
        },
    )

    observation_id = langfuse.get_current_observation_id()

scores = evaluate_answer(user_question, model_answer)

langfuse.create_score(
    trace_id=trace_id,
    observation_id=observation_id,
    name="quality",
    value=scores["quality"],
    data_type="NUMERIC",
    comment="1.0 = good result, 0.0 = bad result",
)

langfuse.create_score(
    trace_id=trace_id,
    observation_id=observation_id,
    name="hallucination",
    value=scores["hallucination"],
    data_type="BOOLEAN",
    comment="Whether the answer appears hallucinated",
)

langfuse.create_score(
    trace_id=trace_id,
    observation_id=observation_id,
    name="relevance",
    value=scores["relevance"],
    data_type="NUMERIC",
    comment="How relevant the answer is to the user's question",
)

langfuse.flush()

print("trace_id:", trace_id)
print("answer:", model_answer)
print("scores:", scores)
