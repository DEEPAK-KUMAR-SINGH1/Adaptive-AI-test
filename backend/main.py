from fastapi import FastAPI
import uuid

from database import cursor, db
from adaptive_engine import update_ability

app = FastAPI()


@app.post("/start-session")
def start_session():

    session_id = str(uuid.uuid4())

    cursor.execute(
        "INSERT INTO user_sessions (session_id, ability_score) VALUES (%s,%s)",
        (session_id,0.5)
    )

    db.commit()

    return {"session_id":session_id}

@app.get("/next-question/{session_id}")
def next_question(session_id: str):

    cursor.execute(
        "SELECT ability_score FROM user_sessions WHERE session_id=%s",
        (session_id,)
    )

    ability = cursor.fetchone()["ability_score"]

    cursor.execute(
        """
        SELECT * FROM questions
        WHERE id NOT IN (
            SELECT question_id FROM responses WHERE session_id=%s
        )
        ORDER BY ABS(difficulty - %s)
        LIMIT 1
        """,
        (session_id, ability)
    )

    question = cursor.fetchone()

    if question is None:
        return {"message": "Test completed"}

    return question

    return cursor.fetchone()

@app.post("/submit-answer")
def submit_answer(data: dict):

    session_id = data["session_id"]
    question_id = data["question_id"]
    answer = data["answer"]

    cursor.execute(
        "SELECT correct_answer FROM questions WHERE id=%s",
        (question_id,)
    )

    correct = cursor.fetchone()["correct_answer"]

    is_correct = answer == correct

    cursor.execute(
        """
        INSERT INTO responses
        (session_id,question_id,selected_answer,is_correct)
        VALUES (%s,%s,%s,%s)
        """,
        (session_id,question_id,answer,is_correct)
    )

    cursor.execute(
        "SELECT ability_score FROM user_sessions WHERE session_id=%s",
        (session_id,)
    )

    ability = cursor.fetchone()["ability_score"]

    ability = update_ability(ability,is_correct)

    cursor.execute(
        "UPDATE user_sessions SET ability_score=%s WHERE session_id=%s",
        (ability,session_id)
    )

    db.commit()

    return {"correct":is_correct,"new_ability":ability}