from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-6"


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat_with_claude(messages):
    message = client.messages.create(
        max_tokens=1000,
        messages=messages,
        model=model,
    )
    return message.content[0].text


# Start with an empty message list
messages = []

while True:
    user_input = input("Type your question or exit to complete > ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    print(">", user_input)
    # Add user input to the conversation history
    add_user_message(messages, user_input)
    # Call Claude with the full conversation history
    answer = chat_with_claude(messages)
    add_assistant_message(messages, answer)
    print(
        "Claude:",
    )
    print("my answer is:", answer)
    print("Continue the conversation or type 'exit' to finish.\n")


# def add_user_message(messages, text):
#     user_message = {"role": "user", "content": text}
#     messages.append(user_message)
#
# def add_assistant_message(messages, text):
#     assistant_message = {"role": "assistant", "content": text}
#     messages.append(assistant_message)
#
# def chat_with_claude(messages):
#     message = client.messages.create(
#         max_tokens=1000,
#         messages=messages,
#         model=model,
#     )
#     return message.content[0].text
#
#
# # Start with an empty message list
# messages = []
#
# # Add the initial user question
# add_user_message(messages, "Define quantum computing in one sentence")
#
# # Get Claude's response
# answer = chat_with_claude(messages)
#
# # Add Claude's response to the conversation history
# add_assistant_message(messages, answer)
#
# # Add a follow-up question
# add_user_message(messages, "Write another sentence")
#
# # Get the follow-up response with full context
# final_answer = chat_with_claude(messages)
#
# add_assistant_message(messages, final_answer)
#
# for i in messages:
#     print(f"{i['role']}: {i['content']}\n")
#
