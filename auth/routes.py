from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Users
import uuid
from schemas import UserResponse, UserCreate
from operations import create_user, get_user_by_id, get_users, update_user, delete_user

router = APIRouter()

# وابستگی برای دریافت سشن دیتابیس
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 دریافت همه کاربران
@router.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

# 📌 دریافت یک کاربر بر اساس ID
@router.get("/users/{user_id}")
def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    try:
        user_uuid = UUID(user_id)  # تبدیل `str` به `UUID`
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    user = db.query(Users).filter(Users.id == user_uuid).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

# 📌 ایجاد کاربر جدید
@router.post("/users", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

# 📌 بروزرسانی اطلاعات کاربر
@router.put("/users/{user_id}", response_model=UserResponse)
def update_existing_user(user_id: str, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

# 📌 حذف کاربر
@router.delete("/users/{user_id}")
def delete_user_by_id(user_id: str, db: Session = Depends(get_db)):
    try:
        user_uuid = UUID(user_id)  # تبدیل `str` به `UUID`
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    user = db.query(Users).filter(Users.id == user_uuid).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    
    return {"message": "User deleted successfully"}
