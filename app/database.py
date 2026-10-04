from sqlalchemy import create_engine ,Column, Integer, String
from sqlalchemy.orm import declarative_base ,sessionmaker
engine = create_engine("sqlite:///./database.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)