# 🧠 Adaptive AI Diagnostic Test Engine

An **AI-powered adaptive testing system** that dynamically adjusts question difficulty based on the student's ability.
The system evaluates a user's performance in real time and estimates their skill level using an **adaptive learning algorithm**.

This project demonstrates how **AI-driven assessment systems** can personalize testing experiences similar to platforms like **GRE, GMAT, and Duolingo English Test**.

---

# 🚀 Features

✅ Adaptive question selection based on student ability
✅ Real-time ability score calculation
✅ AI explanation for incorrect answers
✅ Interactive test interface using Streamlit
✅ Student performance dashboard
✅ Correct vs Wrong answer analytics (Pie Chart)
✅ Accuracy calculation
✅ Question progress tracking

---

# 🧠 How It Works

1. User starts a test session.
2. The system fetches a question based on current ability level.
3. The user submits an answer.
4. The backend evaluates correctness.
5. The student's **ability score is updated**.
6. The next question is selected adaptively.

This creates a **personalized testing experience** where question difficulty evolves according to performance.

---

# 🏗 Project Architecture

```
User (Streamlit UI)
        │
        ▼
Frontend (Streamlit App)
        │
        ▼
FastAPI Backend
        │
        ▼
Question Database (MySQL)
```

---

# 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Python

### Database

* MySQL
* MySQL Workbench

### Data Processing

* Pandas

### Visualization

* Matplotlib

---

# 📊 Dashboard Features

The student dashboard shows:

* Ability Score
* Question Progress
* Accuracy %
* Correct vs Wrong Answer Distribution
* Real-time Performance Analytics

---

# 📂 Project Structure

```
adaptive-ai-test/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── adaptive_engine.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── questions.csv
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/adaptive-ai-test.git
cd adaptive-ai-test
```

---

## 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 3️⃣ Start FastAPI server

```
uvicorn main:app --reload
```

Server will run on:

```
http://localhost:8000
```

---

## 4️⃣ Run Streamlit App

```
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

# 📸 Screenshots

## Test Interface

(Add screenshot here)

## Student Dashboard

(Add screenshot here)

---

# 🎯 Example Output

```
Question 1
What is the output of Python list slicing?

Correct Answer ✅

Ability Score Updated → 0.63
Accuracy → 75%
```

---

# 🧪 Future Improvements

* Ability progress graph
* Difficulty-based question bank
* AI-generated questions using LLM
* Leaderboard system
* Authentication system
* Deployment on cloud

---

# 🤖 Real World Applications

This system can be used for:

* Online education platforms
* Skill assessment tools
* AI-driven hiring tests
* Competitive exam preparation systems
* Personalized learning platforms

---

# 👨‍💻 Author

**Deepak Kumar Singh**

AI Engineer | Data Science | Machine Learning | FastAPI | LLM Applications

---

# ⭐ If you like this project

Give it a **star ⭐ on GitHub** and feel free to contribute!
