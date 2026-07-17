from ollama import chat

from app.brain.history import (
    add_message,
    get_history,
)

SYSTEM_PROMPT = """
You are NEXA, an advanced AI voice assistant.

Rules:
1. Speak naturally like a human.
2. Never invent strange Hindi words.
3. If the user speaks English, reply only in English.
4. If the user speaks Hindi, reply in simple, natural Hindi.
5. Do not mix Hindi and English unless the user does.
6. Keep answers concise (2-5 sentences) unless the user asks for details.
7. Be accurate. If you don't know something, say so instead of making it up.
8. Maintain context from previous messages.
9. Sound friendly and professional.
10. Never repeat yourself.
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
        messages=messages,
    )

    answer = response["message"]["content"].strip()

    add_message("assistant", answer)

    return answer