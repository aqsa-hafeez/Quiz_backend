from fastapi import FastAPI
from app.routes.quiz_routes import router as quiz_router

app = FastAPI(
    title="AI Quiz Generator API",
    description="Generate quizzes and evaluate answers using Groq LLM",
    version="1.0"
)

app.include_router(quiz_router)