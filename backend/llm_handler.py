import os

import google.generativeai as genai

from dotenv import load_dotenv

from backend.config import (
    GEMINI_MODEL_NAME
)


from pathlib import Path
# Load .env file relative to this file
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)


# Read API key
API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


if not API_KEY:

    raise ValueError(
        "GEMINI_API_KEY not found"
    )


# Configure Gemini
genai.configure(
    api_key=API_KEY
)


# Create model
model = genai.GenerativeModel(
    GEMINI_MODEL_NAME
)


def generate_answer(
        question,
        retrieved_context
):
    """
    Generate AI answer.
    """

    prompt = f"""
You are an expert software engineer.

Answer the question using the repository context below.

Repository Context:
{retrieved_context}

Question:
{question}

Rules:
- Mention the relevant file names if they exist in the context.
- Avoid hallucination. Do not invent details about the codebase.
- If the repository context does not contain the answer or specific details to address the question, start your response by saying: "Information not found in the codebase." Then, use your general software engineering expertise to explain the concept generally or suggest how the developer can implement or find it, clearly distinguishing your general advice from the actual repository code.

Answer:
"""

    response = (
        model.generate_content(
            prompt
        )
    )

    return response.text