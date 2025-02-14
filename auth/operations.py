from datetime import datetime
from sqlalchemy.orm import Session
from uuid import UUID
from uuid import uuid4
from models import Users
from sqlalchemy.exc import SQLAlchemyError
from schemas import UserCreate



# ایجاد کاربر جدید

def create_user(db: Session, user: UserCreate):
    new_user = Users(
        id=uuid4(),  # تولید ID تصادفی برای کاربر
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        user_name=user.user_name,
        password=user.password,
        birth_day=user.birth_day,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# پیدا کردن کاربر بر اساس id
def get_user_by_id(db: Session, user_id: UUID):
    return db.query(Users).filter(Users.id == user_id).first()

# گرفتن لیست همه کاربران
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Users).offset(skip).limit(limit).all()

# آپدیت کردن کاربر
def update_user(db: Session, user_id: UUID, first_name: str = None, last_name: str = None, email: str = None, 
                user_name: str = None, password: str = None, birth_day: str = None):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if user_name:
            user.user_name = user_name
        if password:
            user.password = password
        if birth_day:
            user.birth_day = birth_day
        user.updated_at = str(datetime.utcnow())
        
        db.commit()
        db.refresh(user)
        return user
    return None

# حذف کردن کاربر
def delete_user(db: Session, user_id: UUID):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
