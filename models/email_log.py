from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from database.database import Base


class EmailLog(Base):

    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True)

    user_name = Column(String(100))

    user_email = Column(String(150))

    skill = Column(String(100))

    status = Column(String(20))

    error = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )