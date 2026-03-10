from fastapi import APIRouter
from app.models.quiz_models import QuizRequest, QuizCheckRequest
from app.services.quiz_service import generate_quiz, check_quiz

router = APIRouter()


# -----------------------------
# Generate Quiz Endpoint
# -----------------------------

@router.post("/generate-quiz")
def generate_quiz_api(request: QuizRequest):

    result = generate_quiz(request)

    return result


# -----------------------------
# Check Quiz Endpoint
# -----------------------------

@router.post("/check-quiz")
def check_quiz_api(request: QuizCheckRequest):

    result = check_quiz(request)

    return result