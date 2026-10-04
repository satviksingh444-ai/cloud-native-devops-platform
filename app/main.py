from fastapi import FastAPI
from pydantic import BaseModel
from app.database import Base , engine, SessionLocal, UserDB
app = FastAPI()

@app.get("/")
def home():
    return {"message": "DevOps project is running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}


class User(BaseModel):
    name: str
    age: int


@app.post("/users")
def create_user(user: User):
    db = SessionLocal()
    db_user = UserDB(
    name=user.name,
    age=user.age
)
    db.add(db_user)
    db.commit()
    return {
        "message": "User created",
        "user": user
    }