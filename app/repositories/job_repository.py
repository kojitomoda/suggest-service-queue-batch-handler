from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from app.models.job import Job
from app.models.task import Task
from datetime import datetime

class JobRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_jobs_with_task(self):
        """
        ジョブを関連するタスクと一緒に取得
        """
        now = datetime.utcnow()
        return (
            self.db.query(Job, Task)
            .join(Task, Job.task_id == Task.id)
            .filter(
                (Job.available_at <= now) | (Job.failed_at.isnot(None)),
                Job.reserved_at.is_(None),
                Job.searched_at.is_(None)
            )
            .options(joinedload(Job.task))
            .all()
        )