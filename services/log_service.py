from database.database import SessionLocal
from models.email_log import EmailLog
from config import USE_DATABASE


def save_log(
    name,
    email,
    skill,
    status,
    error=None
):

    # Database disabled
    if not USE_DATABASE:
        print("Database disabled. Log skipped.")
        return

    db = SessionLocal()

    try:

        log = EmailLog(
            user_name=name,
            user_email=email,
            skill=skill,
            status=status,
            error=error
        )

        db.add(log)
        db.commit()

    except Exception as e:

        db.rollback()

        print("Database logging failed:", e)

    finally:

        db.close()