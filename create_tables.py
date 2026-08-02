from database.database import Base
from database.database import engine

from models.email_log import EmailLog

Base.metadata.create_all(bind=engine)

print("Tables Created")