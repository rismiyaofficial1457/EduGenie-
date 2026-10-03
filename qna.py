from gemini_client import generate_content


def answer_question(question: str) -> str:

    prompt = f"""
You are EduGenie, a friendly educational assistant.
Answer the student's question clearly and accurately.
Use simple language suitable for a college student.

Student question:
{question}
"""

    result = generate_content(
        prompt,
        temperature=0.5,
        max_output_tokens=800
    )

    # Local fallback if Gemini quota is unavailable
    if (
        "RESOURCE_EXHAUSTED" in result
        or "429" in result
        or "Gemini is temporarily unavailable" in result
    ):
        question_lower = question.lower()

        if "python" in question_lower:
            return """
Python is a high-level programming language.
It is simple, easy to learn, and widely used for web development,
data science, artificial intelligence, automation, and software development.
"""

        return f"""
EduGenie Answer:

Your question is: {question}

This is a temporary local response because the Gemini API
daily quota has been reached.

Please try the question again after the Gemini quota resets.
"""

    return result