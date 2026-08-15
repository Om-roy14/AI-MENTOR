AI Mentor — Setup & Usage

Live Demo: https://ai-mentor-lemon.vercel.app/

AI Mentor generates a personalized learning roadmap based on the user's current skill, career goal, experience, daily study time, and learning style.

Quick Start
# 1. Clone repository
git clone https://github.com/Om-roy14/AI-MENTOR.git
cd AI-MENTOR


# 2. Create virtual environment
python -m venv agentic_env


# 3. Activate environment — Windows
agentic_env\Scripts\activate


# 4. Install dependencies
pip install -r requirements.txt
Environment Variables

Create a .env file in the project root:

USE_DATABASE=true


MYSQL_HOST=your_mysql_host
MYSQL_PORT=your_mysql_port
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=your_mysql_database


EMAIL=your_email
EMAIL_PASSWORD=your_email_password


GROQ_API_KEY=your_groq_api_key

Never commit .env or API/database credentials to GitHub.

Database Setup

If database logging is enabled:

python create_tables.py

This creates the email_logs table used to store roadmap/email activity.

To run without a database:

USE_DATABASE=false
Run Locally
uvicorn app:app --reload

Open:

http://127.0.0.1:8000
How to Use
Enter your Name.
Enter your Email.
Enter your Current Skill.
Enter your Career Goal.
Select your Experience Level.
Enter your Daily Study Time.
Select your Learning Style.
Add optional notes.
Click Generate Roadmap.
AI Mentor generates the personalized roadmap and sends it to the provided email.
If database logging is enabled, the request status is stored in MySQL.
Application Flow
User Input
    ↓
FastAPI Backend
    ↓
Prompt Generation
    ↓
Groq AI
    ↓
Personalized Learning Roadmap
    ↓
Email Service
    ↓
User's Email


              ↓
        MySQL Database
              ↓
          email_logs
Project Structure
AI-MENTOR/
│
├── app.py
├── config.py
├── create_tables.py
├── requirements.txt
├── vercel.json
├── .env
│
├── database/
│   └── database.py
│
├── models/
│   └── email_log.py
│
├── routes/
│   └── mentor.py
│
├── services/
│   ├── ai_service.py
│   ├── email_service.py
│   ├── log_service.py
│   └── prompt_service.py
│
├── static/
│   ├── css/
│   └── images/
│
└── templates/
    ├── index.html
    └── success.html
Database Check

To list tables:

python -c "from database.database import engine; from sqlalchemy import inspect; print(inspect(engine).get_table_names())"

To view email logs:

python -c "from database.database import engine; from sqlalchemy import text; c=engine.connect(); print(c.execute(text('SELECT * FROM email_logs')).fetchall()); c.close()"
Deployment

The project can be deployed to Vercel by importing the GitHub repository and adding the required environment variables in the Vercel project settings.

Required variables:

USE_DATABASE
MYSQL_HOST
MYSQL_PORT
MYSQL_USER
MYSQL_PASSWORD
MYSQL_DATABASE
EMAIL
EMAIL_PASSWORD
GROQ_API_KEY

For cloud deployment, the MySQL database must be accessible from Vercel.

Security
.env
__pycache__/
*.pyc
agentic_env/
.venv/

These should be included in .gitignore.

Live Application: https://ai-mentor-lemon.vercel.app/