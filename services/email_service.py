import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

load_dotenv()


EMAIL = os.getenv("EMAIL")

PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(

    receiver,

    name,

    roadmap

):

    msg = MIMEMultipart()

    msg["Subject"] = "Your AI Mentor Roadmap"

    msg["From"] = EMAIL

    msg["To"] = receiver

    body = f"""

Hello {name},

Your personalized roadmap is below.

{roadmap}

Happy Learning 🚀

"""

    msg.attach(MIMEText(body, "html"))
    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(

            EMAIL,

            PASSWORD

        )

        server.send_message(msg)