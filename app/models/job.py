from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Job(Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey("task.id"), nullable=False)
    available_at = Column(DateTime)
    reserved_at = Column(DateTime, nullable=True)
    searched_at = Column(DateTime, nullable=True)
    failed_at = Column(DateTime, nullable=True)

    # リレーション
    task = relationship("Task", back_populates="jobs")