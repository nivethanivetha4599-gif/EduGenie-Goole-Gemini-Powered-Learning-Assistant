from gemini_client import generate_text


def summarize_text(
    text: str
) -> str:

    text = text.strip()

    if not text:

        return (
            "Please enter text to summarize."
        )


    prompt = f"""
Summarize the following educational
passage.

Requirements:

- Keep the important facts
- Remove unnecessary repetition
- Make it useful for revision
- Use simple language
- Preserve important context

Passage:

{text}
"""


    return generate_text(
        prompt,

        system_instruction="""
You are EduGenie, a study-notes assistant.

Turn long educational material into
clear and useful revision notes.
"""
    )