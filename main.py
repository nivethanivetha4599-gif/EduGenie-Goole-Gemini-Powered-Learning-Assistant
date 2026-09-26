from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from explanation_module import explain_concept
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)


# ---------------------------------------------------------
# Static files
# ---------------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# ---------------------------------------------------------
# Request models
# ---------------------------------------------------------

class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


class QuizRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


# ---------------------------------------------------------
# Home page
# ---------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request":request}
    )


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "application": "EduGenie"
    }


# ---------------------------------------------------------
# Question Answering
# ---------------------------------------------------------

@app.post("/qa")
async def qa(payload: TextRequest):

    result = answer_question(payload.text)

    return {
        "result": result
    }


# ---------------------------------------------------------
# Concept Explanation
# ---------------------------------------------------------

@app.post("/explain")
async def explain(payload: TextRequest):

    result = explain_concept(payload.text)

    return {
        "result": result
    }


# ---------------------------------------------------------
# Quiz Generation
# ---------------------------------------------------------

@app.post("/quiz")
async def quiz(payload: QuizRequest):

    result = generate_quiz(payload.text)

    return {
        "quiz": result
    }


# ---------------------------------------------------------
# Summarization
# ---------------------------------------------------------

@app.post("/summarize")
async def summarize(payload: TextRequest):

    result = summarize_text(payload.text)

    return {
        "result": result
    }


# ---------------------------------------------------------
# Learning Recommendations
# ---------------------------------------------------------

@app.post("/learn/recommendations")
async def learning_recommendations(payload: TextRequest):

    result = get_learning_recommendations(
        payload.text
    )

    return {
        "result": result
    }