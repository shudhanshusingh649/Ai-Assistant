import os

from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Create Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(question):

    prompt = f"""
Answer this question in only 2-3 short sentences.

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()