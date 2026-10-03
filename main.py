from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="EduGenie",
    description="AI-powered educational assistant",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


class TextRequest(BaseModel):
    text: str


class QuestionRequest(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "EduGenie"
    }


@app.post("/qa")
def qa(data: QuestionRequest):
    return {
        "answer": answer_question(data.question)
    }


@app.post("/explain")
def explain(data: TextRequest):
    return {
        "explanation": explain_topic(data.text)
    }


@app.post("/quiz")
def quiz(data: TextRequest):
    return generate_quiz(data.text)


@app.post("/summarize")
def summarize(data: TextRequest):
    return {
        "summary": summarize_text(data.text)
    }


@app.post("/learn/recommendations")
def learning_recommendations(data: TextRequest):
    return {
        "recommendations": recommend_learning(data.text)
    }
