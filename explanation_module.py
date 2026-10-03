from gemini_client import generate_content

def explain_topic(text: str) -> str:

    prompt = f"""
Explain the following topic clearly for a college student.

- Start with a simple definition.
- Explain the main points.
- Give one simple example.
- Use easy English.

Topic:
{text}
"""

    result = generate_content(
        prompt,
        temperature=0.5,
        max_output_tokens=1000
    )

    # Local fallback if Gemini quota is unavailable
    if (
        "RESOURCE_EXHAUSTED" in result
        or "429" in result
        or "Gemini is temporarily unavailable" in result
    ):
        return f"""
Explanation: {text}

{text} is an important concept in computer science.

Simple explanation:
This topic can be understood by learning its basic meaning,
main concepts, and practical uses.

Example:
Learn the basic definition first, then study a simple example
to understand how the concept works.
"""

    return result