from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'data' / 'database.db'}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)