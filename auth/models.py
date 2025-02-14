from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String)
    last_name = Column(String, default="")
    email = Column(String)
    user_name = Column(String)
    password = Column(String)
    birth_day = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
