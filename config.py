import os
from dotenv import load_dotenv

load_dotenv()


# =========================
# DATABASE
# =========================

USE_DATABASE = os.getenv("USE_DATABASE", "false").lower() == "true"

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


# =========================
# EMAIL
# =========================

EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# =========================
# AI
# =========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")