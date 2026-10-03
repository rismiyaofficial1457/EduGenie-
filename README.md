# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS educational assistant based on the project document.

## Features

- Ask questions with Gemini
- Explain concepts using local LaMini-Flan-T5-783M
- Generate exactly 3 MCQs with 4 options each
- Summarize educational passages
- Generate a beginner-to-advanced learning path
- Browser-based responsive interface
- REST API endpoints for every module

## Project structure

EduGenie/
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css

## Requirements

- Python 3.10 or newer
- Internet connection for Gemini API and the first LaMini model download
- A Gemini API key for Gemini-powered modules
- About 4 GB or more free disk space is recommended for the local LaMini model and Python packages

## Windows setup

Open Command Prompt/PowerShell in this folder:

```text
python --version
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and put your Gemini API key in it.

Then start the application:

```text
uvicorn main:app --reload
```

Open:

http://127.0.0.1:8000

## macOS/Linux setup

```text
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

Open:

http://127.0.0.1:8000

## API endpoints

POST /qa
Body:
{"question": "What is photosynthesis?"}

POST /explain
Body:
{"text": "Explain photosynthesis"}

POST /quiz
Body:
{"text": "Photosynthesis is the process..."}

POST /summarize
Body:
{"text": "Long educational passage..."}

POST /learn/recommendations
Body:
{"text": "SQL"}

GET /health

## Important first-run behavior

The explanation module downloads the LaMini-Flan-T5-783M model from Hugging Face the first time that endpoint is used. The model is roughly 3.1 GB in its PyTorch form, so the first explanation request can take time and needs sufficient storage.

The other four AI features use the Gemini API.

## Troubleshooting

### "GEMINI_API_KEY is not configured"

Make sure the file is named `.env` and contains:

GEMINI_API_KEY=your_key_here

Restart uvicorn after changing `.env`.

### LaMini installation/model error

Upgrade packages:

```text
python -m pip install --upgrade torch transformers sentencepiece safetensors
```

Then restart the server.

### Port 8000 already in use

Use:

```text
uvicorn main:app --reload --port 8001
```

Then open:

http://127.0.0.1:8001

## Academic project mapping

Milestone 1:
- Model selection
- FastAPI architecture
- Local LaMini model + Gemini API

Milestone 2:
- qna.py
- explanation_module.py
- quiz_module.py
- summary_module.py
- learning_path.py
- FastAPI endpoints in main.py

Milestone 3:
- templates/index.html
- static/style.css
- JavaScript fetch integration

Milestone 4:
- Local uvicorn deployment
- Functional testing of all five features
