from dotenv import load_dotenv
from anthropic import Anthropic
import anthropic

load_dotenv()
client = Anthropic()
# model = "claude-haiku-4-5"
model = "claude-sonnet-4-6"

from get_current_datetime import get_current_datetime_schema, process_tool_call

client = anthropic.Anthropic()

# 1. Send prompt with the tool available
response = client.messages.create(
    model=model,
    max_tokens=1024,
    tools=[get_current_datetime_schema],
    messages=[{"role": "user", "content": "What is the current date and time?"}],
)

# 2. If the model decided to use the tool, execute it and send the result back
if response.stop_reason == "tool_use":
    tool_use_block = next(b for b in response.content if b.type == "tool_use")

    tool_result = process_tool_call(tool_use_block.name, tool_use_block.input)

    # 3. Continue the conversation with the tool result
    final_response = client.messages.create(
        model=model,
        max_tokens=1024,
        tools=[get_current_datetime_schema],
        messages=[
            {"role": "user", "content": "What is the current date and time?"},
            {"role": "assistant", "content": response.content},
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_use_block.id,
                        "content": tool_result,
                    }
                ],
            },
        ],
    )
    print(final_response.content[0].text)
else:
    print(response.content[0].text)
