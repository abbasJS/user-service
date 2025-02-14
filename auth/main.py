from fastapi import FastAPI
from routes import router
from database import Base, engine

# ایجاد جداول در دیتابیس در صورت عدم وجود
Base.metadata.create_all(bind=engine)


app = FastAPI()

# اضافه کردن روت‌ها
app.include_router(router)

# صفحه خوش‌آمدگویی (اختیاری، برای تست و تست‌های اولیه)
@app.get("/")
def read_root():
    return {"message": "Welcome to the User Service API!"}

