from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, autoincrement=True)
    search_word = Column(String, nullable=False)
    search_engine = Column(String, nullable=False)

    # リレーション
    jobs = relationship("Job", back_populates="task")