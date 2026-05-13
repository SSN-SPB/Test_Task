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

# Ollama exposes an OpenAI-compatible API on localhost
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Ollama doesn't require a real key
)

user_question = "What is Langfuse used for?"

trace_id = langfuse.create_trace_id()

with langfuse.start_as_current_observation(
    name="real-qa",
    as_type="generation",
    trace_context={"trace_id": trace_id},
    input={"question": user_question},
):
    response = client.chat.completions.create(
        model="llama3",
        messages=[{"role": "user", "content": user_question}],
    )

    model_answer = response.choices[0].message.content

    # Ollama may or may not return usage; handle gracefully
    usage = response.usage
    usage_details = {}
    if usage:
        usage_details = {
            "input": usage.prompt_tokens or 0,
            "output": usage.completion_tokens or 0,
            "total": usage.total_tokens or 0,
        }

    langfuse.update_current_generation(
        output={"answer": model_answer},
        model="llama3",
        usage_details=usage_details if usage_details else None,
    )

langfuse.flush()
print("Answer:", model_answer)
