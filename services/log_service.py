from database.database import SessionLocal
from models.email_log import EmailLog


def save_log(
    name,
    email,
    skill,
    status,
    error=None
):

    if SessionLocal is None:
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

    except Exception:

        db.rollback()
        raise

    finally:

        db.close()