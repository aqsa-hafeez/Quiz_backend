from pydantic import BaseModel
from typing import List, Optional


# -----------------------------
# Quiz Generation Models
# -----------------------------

class QuizRequest(BaseModel):
    topic: str
    number_of_questions: int
    question_type: str
    complexity: str


class Question(BaseModel):
    question: str
    options: Optional[List[str]] = None
    answer: str


class QuizResponse(BaseModel):
    topic: str
    complexity: str
    questions: List[Question]


# -----------------------------
# Quiz Checking Models
# -----------------------------

class SubmittedAnswer(BaseModel):
    question: str
    correct_answer: str
    student_answer: str


class QuizCheckRequest(BaseModel):
    topic: str
    answers: List[SubmittedAnswer]


class QuizCheckResponse(BaseModel):
    topic: str
    total_questions: int
    correct_answers: int
    score_percentage: float