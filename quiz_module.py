import json
from gemini_client import generate_content


def generate_quiz(text: str):

    prompt = f"""
Create exactly 3 multiple-choice questions from the study material below.

Return ONLY valid JSON in this format:
{{
  "questions": [
    {{
      "question": "Question text",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": "Option A"
    }}
  ]
}}

Study material:
{text}
"""

    result = generate_content(
        prompt,
        temperature=0.3,
        max_output_tokens=1400
    )

    # Local fallback if Gemini quota is unavailable
    if (
        "RESOURCE_EXHAUSTED" in result
        or "429" in result
        or "Gemini is temporarily unavailable" in result
    ):
        return {
            "questions": [
                {
                    "question": "What is Python?",
                    "options": [
                        "A programming language",
                        "A database",
                        "An operating system",
                        "A web browser"
                    ],
                    "answer": "A programming language"
                },
                {
                    "question": "Which symbol is used for comments in Python?",
                    "options": [
                        "#",
                        "//",
                        "/*",
                        "<!--"
                    ],
                    "answer": "#"
                },
                {
                    "question": "Which keyword is used to define a function in Python?",
                    "options": [
                        "def",
                        "function",
                        "func",
                        "define"
                    ],
                    "answer": "def"
                }
            ]
        }

    try:
        # Remove markdown code fences if Gemini adds them
        clean_result = result.strip()

        if clean_result.startswith("```"):
            clean_result = clean_result.replace("```json", "")
            clean_result = clean_result.replace("```", "")
            clean_result = clean_result.strip()

        data = json.loads(clean_result)

        questions = data.get("questions", [])

        if len(questions) != 3:
            raise ValueError()

        for q in questions:
            if len(q.get("options", [])) != 4:
                raise ValueError()

            if q.get("answer") not in q["options"]:
                raise ValueError()

        return {"questions": questions}

    except Exception:
        return {
            "questions": [
                {
                    "question": "What is Python?",
                    "options": [
                        "A programming language",
                        "A database",
                        "An operating system",
                        "A web browser"
                    ],
                    "answer": "A programming language"
                },
                {
                    "question": "Which symbol is used for comments in Python?",
                    "options": [
                        "#",
                        "//",
                        "/*",
                        "<!--"
                    ],
                    "answer": "#"
                },
                {
                    "question": "Which keyword is used to define a function in Python?",
                    "options": [
                        "def",
                        "function",
                        "func",
                        "define"
                    ],
                    "answer": "def"
                }
            ]
        }