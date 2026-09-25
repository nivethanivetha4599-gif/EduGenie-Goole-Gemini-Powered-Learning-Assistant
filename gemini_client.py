from functools import lru_cache

from google import genai
from google.genai import types

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)


class GeminiConfigurationError(
    RuntimeError
):
    pass


@lru_cache(maxsize=1)
def get_client():

    if not GEMINI_API_KEY:

        raise GeminiConfigurationError(
            "GEMINI_API_KEY is not configured. "
            "Create a .env file and add your Gemini API key."
        )

    return genai.Client(
        api_key=GEMINI_API_KEY
    )


# ---------------------------------------------------------
# Normal text generation
# ---------------------------------------------------------

def generate_text(
    prompt: str,
    system_instruction: str | None = None
) -> str:

    client = get_client()

    config = types.GenerateContentConfig(
        temperature=0.4,
        max_output_tokens=2048,
        system_instruction=system_instruction,
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=config,
    )

    text = getattr(
        response,
        "text",
        None
    )

    if not text:

        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return text.strip()


# ---------------------------------------------------------
# JSON generation
# ---------------------------------------------------------

def generate_json(
    prompt: str,
    response_schema
) -> str:

    client = get_client()

    config = types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=3000,
        response_mime_type="application/json",
        response_schema=response_schema,
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=config,
    )

    text = getattr(
        response,
        "text",
        None
    )

    if not text:

        raise RuntimeError(
            "Gemini returned an empty JSON response."
        )

    return text.strip()