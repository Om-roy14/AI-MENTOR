# 🚀 AI Mentor - Personalized Skill Mastery Roadmap Generator

AI Mentor is an AI-powered web application that generates a personalized learning roadmap for any skill and delivers it directly to the user's email as a beautifully formatted HTML email.

The application collects user information through a web interface, uses an LLM (Groq Llama 3.3) to generate a customized roadmap, and automatically emails the roadmap using Gmail SMTP.

---

## ✨ Features

- 🎯 Personalized AI-generated learning roadmap
- 📧 Automatic HTML email delivery
- 🤖 Powered by Groq Llama 3.3
- ⚡ FastAPI backend
- 🎨 Clean and responsive frontend
- 🔒 Environment variable support using `.env`
- 📨 Beautiful HTML email template

---

## 📸 Demo Workflow

```
User fills the form
        │
        ▼
FastAPI Backend
        │
        ▼
Prompt Engineering
        │
        ▼
Groq Llama 3.3
        │
        ▼
Generate Personalized Roadmap
        │
        ▼
Send HTML Email
        │
        ▼
Success Page
```

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3

### Backend

- FastAPI
- Python

### AI

- Groq API
- Llama 3.3 70B Versatile

### Email

- Gmail SMTP
- HTML Email

### Others

- Jinja2
- python-dotenv
- OpenAI Python SDK

---

## 📂 Project Structure

```
AI-MENTOR/
│
├── app.py
├── .env
├── requirements.txt
│
├── routes/
│   └── mentor.py
│
├── services/
│   ├── ai_service.py
│   ├── email_service.py
│   └── prompt_service.py
│
├── templates/
│   ├── index.html
│   ├── roadmap_email.html
│   └── success.html
│
└── static/
    ├── css/
    │   └── style.css
    └── images/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Om-roy14/AI-MENTOR

cd AI-Mentor
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```
### note -- i am using the general env and it might contain several dependencies that might not be used

---

### Configure Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

EMAIL=YOUR_EMAIL@gmail.com

EMAIL_PASSWORD=YOUR_GMAIL_APP_PASSWORD
```

---

### Run the Application

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

## 📧 How It Works

1. User enters their details.
2. FastAPI receives the request.
3. A personalized prompt is generated.
4. Groq Llama 3.3 creates a custom learning roadmap.
5. The roadmap is converted into a beautiful HTML email.
6. Gmail SMTP sends the roadmap to the user's email.
7. User receives a professionally formatted roadmap.

---

## 💡 Example Use Cases

- Learning AI/ML
- Web Development
- Data Science
- UI/UX Design
- Public Speaking
- Content Creation
- Digital Marketing
- Cooking
- Music
- Photography
- Any technical or non-technical skill

---

## 📈 Future Improvements

- User Authentication
- Roadmap History
- Download Roadmap as PDF
- Progress Tracking
- Multiple AI Model Support
- Dashboard
- Docker Deployment
- Cloud Database Integration

---

## 👨‍💻 Author

**Om Kumar Roy**

B.Tech CSE (AI & ML)

Passionate about AI, Machine Learning, LLMs, Agentic AI, and Full Stack Development.

---

## ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.