"""
Basic endpoint smoke tests.

Run after starting the application in another terminal:
    python test_api.py
"""

import json
import urllib.request

BASE = "http://127.0.0.1:8000"


def post(path, payload):
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        BASE + path,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.status, response.read().decode("utf-8")


def get(path):
    with urllib.request.urlopen(BASE + path, timeout=20) as response:
        return response.status, response.read().decode("utf-8")


if __name__ == "__main__":
    status, body = get("/health")
    print("HEALTH:", status, body)

    status, body = post("/qa", {"question": "What is an algorithm?"})
    print("QA:", status, body[:500])

    status, body = post("/summarize", {
        "text": "An algorithm is a finite sequence of clear steps used to solve a problem."
    })
    print("SUMMARY:", status, body[:500])

    status, body = post("/quiz", {
        "text": "Python is a high-level programming language. It is widely used for web development, data analysis, automation, and artificial intelligence."
    })
    print("QUIZ:", status, body[:1000])

    status, body = post("/learn/recommendations", {"text": "SQL"})
    print("LEARNING PATH:", status, body[:700])

    # The local model can take longer on its first call.
    status, body = post("/explain", {"text": "photosynthesis"})
    print("EXPLAIN:", status, body[:700])
