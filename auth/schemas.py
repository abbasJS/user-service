from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: Optional[str] = ''
    email: EmailStr
    user_name: str
    birth_day: Optional[datetime]

class UserCreate(UserBase):
    password: str  # هنگام ایجاد کاربر، نیاز به رمز عبور داریم

class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # برای تبدیل SQLAlchemy به Pydantic
