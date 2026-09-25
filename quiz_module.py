import re

from pydantic import BaseModel, Field

from gemini_client import generate_json


# ---------------------------------------------------------
# Quiz models
# ---------------------------------------------------------

class QuizQuestion(BaseModel):

    question: str

    options: list[str] = Field(
        min_length=4,
        max_length=4
    )

    correct_answer: str

    explanation: str


class Quiz(BaseModel):

    questions: list[QuizQuestion] = Field(
        min_length=3,
        max_length=3
    )


# ---------------------------------------------------------
# Clean markdown JSON
# ---------------------------------------------------------

def clean_json_block(
    text: str
) -> str:

    text = text.strip()

    text = re.sub(
        r"^```(?:json)?\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    return text.strip()


# ---------------------------------------------------------
# Generate quiz
# ---------------------------------------------------------

def generate_quiz(
    passage: str
) -> dict:

    passage = passage.strip()

    if not passage:

        return {
            "questions": []
        }


    prompt = f"""
Create exactly 3 multiple-choice questions
from the educational text below.

Requirements:

- Exactly 3 questions
- Exactly 4 options per question
- Only one correct answer
- correct_answer must exactly match one option
- Include a short explanation
- Questions must test understanding
- Avoid trick questions

Educational text:

{passage}
"""


    try:

        raw = generate_json(
            prompt,
            Quiz
        )

        cleaned = clean_json_block(
            raw
        )

        quiz = Quiz.model_validate_json(
            cleaned
        )

        return quiz.model_dump()


    except Exception as exc:

        return {
            "questions": [],

            "error": (
                "Quiz generation failed: "
                f"{type(exc).__name__}: {exc}"
            )
        }