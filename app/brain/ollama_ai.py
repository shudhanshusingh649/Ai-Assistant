from ollama import chat

from app.brain.history import (
    add_message,
    get_history,
)


SYSTEM_PROMPT = """
You are NEXA.

You are a smart AI assistant.

Always reply naturally.

If the previous conversation contains context,
use it.

Reply in the same language as the user.

If user speaks Hindi,
reply in Hindi.

Keep answers short unless user asks for detail.
"""


def ask_ai(question):

    add_message("user", question)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(get_history())

    response = chat(
        model="llama3.2",
        messages=messages
    )

    answer = response["message"]["content"]

    add_message("assistant", answer)

    return answer