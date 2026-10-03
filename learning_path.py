from gemini_client import generate_content


def recommend_learning(text: str) -> str:

    prompt = f"""
Create a practical learning path for a college student based on the topic below.

Include:
1. What to learn first
2. Important concepts
3. Practice activities
4. Suggested order of learning
5. A simple next step

Keep it realistic, clear, and beginner-friendly.

Topic or goal:
{text}
"""

    result = generate_content(
        prompt,
        temperature=0.6,
        max_output_tokens=1000
    )

    # If Gemini quota is unavailable, use a local fallback
    if (
        "RESOURCE_EXHAUSTED" in result
        or "429" in result
        or "Gemini is temporarily unavailable" in result
    ):
        return f"""
Learning Path for: {text}

1. Start with the Basics
- Understand the meaning and purpose of {text}.
- Learn the basic terms and concepts.

2. Learn Important Concepts
- Study the main concepts related to {text}.
- Understand how each concept works.
- Learn simple examples.

3. Practice
- Try small practical exercises.
- Solve simple problems related to {text}.
- Review your mistakes and improve.

4. Suggested Learning Order
- Basics
- Important concepts
- Examples
- Practice
- Mini project

5. Next Step
- Practice {text} for 20–30 minutes.
- Then move to an intermediate-level example or mini project.
"""

    return result