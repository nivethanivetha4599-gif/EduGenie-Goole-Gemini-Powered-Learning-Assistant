from gemini_client import generate_text


def get_learning_recommendations(
    topic: str
) -> str:

    topic = topic.strip()

    if not topic:

        return "Please enter a topic."


    prompt = f"""
Create a structured learning path
for the following topic:

{topic}

Organize the learning path into:

1. Prerequisites
2. Beginner level
3. Intermediate level
4. Advanced level
5. Practical projects
6. Practice activities
7. Suggested resource types
8. Suggested timeline

Start from beginner level unless
another level is specified.

Make the plan practical and easy
to follow.

Do not invent specific URLs.
"""


    return generate_text(
        prompt,

        system_instruction="""
You are EduGenie, an educational
learning-path designer.

Create realistic, structured,
progressive learning plans.
"""
    )