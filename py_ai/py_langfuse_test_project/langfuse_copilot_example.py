import os

from dotenv import load_dotenv
from langfuse import Langfuse

load_dotenv()

langfuse = Langfuse(
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    host=os.environ["LANGFUSE_BASE_URL"],
)

trace_id = langfuse.create_trace_id()

with langfuse.start_as_current_observation(
    name="python-example",
    as_type="generation",
    trace_context={"trace_id": trace_id},
    input={"query": "hello world"},
):
    langfuse.update_current_generation(
        output={"message": "done"},
        model="demo-model",
        usage_details={
            "input": 5,
            "output": 2,
            "total": 7,
        },
    )

    observation_id = langfuse.get_current_observation_id()

langfuse.create_score(
    trace_id=trace_id,
    observation_id=observation_id,
    name="quality",
    value=1.0,
    comment="Successful run",
)

langfuse.flush()
print("done, trace_id =", trace_id)
