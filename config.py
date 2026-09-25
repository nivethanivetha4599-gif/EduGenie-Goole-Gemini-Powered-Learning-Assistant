import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent

ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


# ---------------------------------------------------------
# Gemini configuration
# ---------------------------------------------------------

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
).strip()


GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
).strip()


# ---------------------------------------------------------
# Local explanation model
# ---------------------------------------------------------

LOCAL_EXPLANATION_MODEL = os.getenv(
    "LOCAL_EXPLANATION_MODEL",
    "MBZUAI/LaMini-Flan-T5-783M"
).strip()


# ---------------------------------------------------------
# Local model switch
# ---------------------------------------------------------

ENABLE_LOCAL_EXPLANATION = (
    os.getenv(
        "ENABLE_LOCAL_EXPLANATION",
        "true"
    ).lower()
    == "true"
)