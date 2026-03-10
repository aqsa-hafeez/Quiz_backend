from groq import Groq
from app.core.config import settings
import json
import re

client = Groq(api_key=settings.GROQ_API_KEY)


def extract_json(text):
    """
    Extract JSON from LLM response
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError("No valid JSON found")


def generate_quiz(data):

    prompt = f"""
Generate a quiz.

Topic: {data.topic}
Number of Questions: {data.number_of_questions}
Question Type: {data.question_type}
Difficulty: {data.complexity}

Return ONLY JSON.

Structure:

{{
 "topic": "{data.topic}",
 "complexity": "{data.complexity}",
 "questions":[
   {{
     "question": "question text",
     "options": ["A","B","C","D"],
     "answer": "correct answer"
   }}
 ]
}}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_completion_tokens=1024
    )

    response_text = completion.choices[0].message.content

    return extract_json(response_text)


# -----------------------------
# Check Quiz Answers
# -----------------------------

def check_quiz(data):

    prompt = f"""
Evaluate student answers.

Return ONLY JSON:

{{
 "topic": "{data.topic}",
 "total_questions": number,
 "correct_answers": number,
 "score_percentage": percentage
}}

Answers:
{data.answers}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    response_text = completion.choices[0].message.content

    return extract_json(response_text)