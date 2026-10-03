import os
import time

from dotenv import load_dotenv
from google import genai


# Load .env file
load_dotenv()


# Gemini API settings
API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()


if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Please add your Gemini API key to the .env file."
    )


# Create Gemini client
client = genai.Client(api_key=API_KEY)


def generate_content(
    prompt: str,
    temperature: float = 0.7,
    max_output_tokens: int = 1000,
    retries: int = 3,
) -> str:
    """
    Generate a response from Gemini.

    Automatically retries temporary 503/429 errors.
    """

    last_error = None

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config={
                    "temperature": temperature,
                    "max_output_tokens": max_output_tokens,
                },
            )

            if response.text:
                return response.text.strip()

            return "Sorry, Gemini returned an empty response."

        except Exception as error:
            last_error = error
            error_text = str(error)

            # Retry temporary server/rate-limit errors
            if "503" in error_text or "UNAVAILABLE" in error_text:
                if attempt < retries - 1:
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                    continue

            if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
                if attempt < retries - 1:
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                    continue

            break

    return (
        "Gemini is temporarily unavailable. "
        "Please try again in a few seconds."
        f"\n\nTechnical error: {last_error}"
    )