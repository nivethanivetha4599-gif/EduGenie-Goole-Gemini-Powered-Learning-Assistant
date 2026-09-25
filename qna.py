from gemini_client import generate_text


def answer_question(question: str) -> str:

    question = question.strip()

    if not question:

        return "Please enter a question."


    prompt = f"""
Answer the student's question accurately
and concisely.

Explain important reasoning when useful.

If the question is ambiguous, clearly
state the assumption you used.

Question:

{question}
"""


    return generate_text(
        prompt,

        system_instruction="""
You are EduGenie, an educational AI assistant.

Your job is to help students understand
academic and general knowledge topics.

Use simple language.

Be accurate.

Do not invent sources.

When appropriate, give examples.
"""
    )