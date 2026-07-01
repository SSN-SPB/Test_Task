import os
from dotenv import load_dotenv
from langfuse import Langfuse
from anthropic import Anthropic
from opentelemetry.instrumentation.anthropic import AnthropicInstrumentor


load_dotenv()

# Debug check
print("Anthropic key loaded:", os.getenv("ANTHROPIC_API_KEY") is not None)

# Enable tracing
AnthropicInstrumentor().instrument()

# Init Langfuse
langfuse = Langfuse()

# Explicit API key passing
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in one two sentence"}],
)

print(response.content[0].text)

langfuse.flush()
