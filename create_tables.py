from database.database import Base, engine
from models.email_log import EmailLog
from config import USE_DATABASE


if not USE_DATABASE:

    print("Database is disabled.")
    print("Set USE_DATABASE=true in .env to create tables.")

else:

    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully.")