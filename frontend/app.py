import streamlit as st
import requests
import matplotlib.pyplot as plt

API = "http://localhost:8000"

st.set_page_config(page_title="Adaptive AI Test", layout="wide")

st.title("🧠 Adaptive AI Diagnostic Test")

# ---------- SESSION INIT ----------
if "session" not in st.session_state:
    st.session_state.session = None
    st.session_state.question = None
    st.session_state.result = None
    st.session_state.ability = 0.5
    st.session_state.q_count = 0
    st.session_state.correct_count = 0
    st.session_state.wrong_count = 0


# ---------- SIDEBAR ----------
with st.sidebar:

    st.header("📊 Student Dashboard")

    if st.session_state.session:

        st.metric("Ability Score", round(st.session_state.ability,2))

        progress = st.session_state.q_count / 10
        st.progress(progress)

        st.write(f"Questions Answered: {st.session_state.q_count} / 10")

        st.divider()

        # Performance Stats
        correct = st.session_state.correct_count
        wrong = st.session_state.wrong_count

        st.write(f"✅ Correct: {correct}")
        st.write(f"❌ Wrong: {wrong}")

        if correct + wrong > 0:

            labels = ["Correct", "Wrong"]
            sizes = [correct, wrong]

            fig, ax = plt.subplots()
            ax.pie(
                sizes,
                labels=labels,
                autopct='%1.0f%%',
                startangle=90
            )
            ax.axis("equal")

            st.pyplot(fig)

            accuracy = (correct / (correct + wrong)) * 100
            st.metric("Accuracy", f"{accuracy:.1f}%")

    else:
        st.write("Start test to see stats")


# ---------- START TEST ----------
if st.session_state.session is None:

    if st.button("🚀 Start Test"):

        r = requests.post(f"{API}/start-session")

        st.session_state.session = r.json()["session_id"]
        st.session_state.question = None
        st.session_state.q_count = 0
        st.session_state.correct_count = 0
        st.session_state.wrong_count = 0


# ---------- FETCH QUESTION ----------
if st.session_state.session:

    if st.session_state.question is None:

        r = requests.get(
            f"{API}/next-question/{st.session_state.session}"
        )

        data = r.json()

        if "message" in data:
            st.success("🎉 Test Completed!")
            st.stop()

        st.session_state.question = data


    q = st.session_state.question

    st.subheader(f"Question {st.session_state.q_count + 1}")

    st.write(q["question_text"])


    options = {
        "A": q["option_a"],
        "B": q["option_b"],
        "C": q["option_c"],
        "D": q["option_d"]
    }


    option = st.radio(
        "Select your answer",
        options=list(options.keys()),
        format_func=lambda x: f"{x}) {options[x]}"
    )


    # ---------- SUBMIT ----------
    if st.button("Submit Answer"):

        result = requests.post(
            f"{API}/submit-answer",
            json={
                "session_id": st.session_state.session,
                "question_id": q["id"],
                "answer": option
            }
        ).json()

        st.session_state.result = result
        st.session_state.ability = result["new_ability"]
        st.session_state.q_count += 1

        if result["correct"]:
            st.session_state.correct_count += 1
        else:
            st.session_state.wrong_count += 1


    # ---------- SHOW RESULT ----------
    if st.session_state.result:

        result = st.session_state.result

        if result["correct"]:
            st.success("✅ Correct Answer")
        else:
            st.error("❌ Wrong Answer")

            if "explanation" in result and result["explanation"]:
                st.info(result["explanation"])

        st.write("Updated Ability Score:", round(result["new_ability"],2))


        # ---------- NEXT QUESTION ----------
        if st.button("Next Question ➡️"):

            st.session_state.question = None
            st.session_state.result = None
            st.rerun()