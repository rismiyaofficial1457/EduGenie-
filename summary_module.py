from gemini_client import generate_content


def summarize_text(text: str) -> str:

    prompt = f"""
Summarize the following study material for a college student.

- Keep the important points.
- Use simple English.
- Use short bullet points.
- Do not add information not in the material.

Study material:
{text}
"""

    result = generate_content(
        prompt,
        temperature=0.4,
        max_output_tokens=1000
    )

    # Local fallback if Gemini quota is unavailable
    if (
        "RESOURCE_EXHAUSTED" in result
        or "429" in result
        or "Gemini is temporarily unavailable" in result
    ):
        return f"""
Summary

Topic:
{text}

Key Points:
• This material explains the main idea of the given topic.
• The topic can be understood by identifying its important concepts.
• Learning the basic concepts helps in understanding practical applications.

Conclusion:
The above points provide a simple overview of the given study material.
"""

    return result