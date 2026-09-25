from functools import lru_cache

from config import (
    ENABLE_LOCAL_EXPLANATION,
    LOCAL_EXPLANATION_MODEL
)

from gemini_client import generate_text


# ---------------------------------------------------------
# Load local model only when needed
# ---------------------------------------------------------

@lru_cache(maxsize=1)
def get_local_pipeline():

    from transformers import pipeline

    return pipeline(
        "text2text-generation",

        model=LOCAL_EXPLANATION_MODEL,

        tokenizer=LOCAL_EXPLANATION_MODEL
    )


# ---------------------------------------------------------
# Local explanation
# ---------------------------------------------------------

def local_explanation(
    topic: str
) -> str:

    prompt = f"""
Explain the following educational concept
to a beginner.

Use simple language.

Use short sentences.

Give one small example.

Avoid unnecessary technical terminology.

Concept:

{topic}
"""

    pipeline = get_local_pipeline()

    result = pipeline(
        prompt,
        max_new_tokens=220,
        do_sample=False
    )

    return result[0][
        "generated_text"
    ].strip()


# ---------------------------------------------------------
# Main explanation function
# ---------------------------------------------------------

def explain_concept(
    topic: str
) -> str:

    topic = topic.strip()

    if not topic:

        return "Please enter a topic to explain."


    # Try local model first
    if ENABLE_LOCAL_EXPLANATION:

        try:

            return local_explanation(
                topic
            )

        except Exception:

            # Fall back to Gemini
            pass


    # Gemini fallback
    prompt = f"""
Explain the following concept to a beginner.

Topic:

{topic}

Structure the response as:

1. Simple definition
2. Important points
3. Simple example
4. Short recap

Use easy-to-understand language.
"""


    return generate_text(
        prompt,

        system_instruction="""
You are EduGenie, a patient educational tutor.

Explain difficult concepts in a simple way.

The learner may have no previous knowledge.
"""
    )