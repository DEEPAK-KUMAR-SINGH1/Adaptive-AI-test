import os
from langchain_mistralai import ChatMistralAI

client = ChatMistralAI(api_key=os.getenv("MISTRAL_API_KEY"))

def generate_study_plan(weak_topics, ability):

    prompt = f"""
    Student ability score: {ability}

    Weak topics: {weak_topics}

    Generate a 3 step study plan.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content