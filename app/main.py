import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.repositories.job_repository import JobRepository
from app.util.logger import get_module_logger

# 環境変数からDATABASE_URLとUAを取得
DATABASE_URL = os.getenv("DATABASE_URL")
USER_AGENT = os.getenv("USER_AGENT", "default-user-agent")  # UAのデフォルト値設定

# データベース接続設定
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger = get_module_logger(__name__)

def lambda_handler(event, context):
    session = SessionLocal()
    try:
        job_repo = JobRepository(session)
        jobs = job_repo.get_jobs_with_task()

        sqs_payloads = [
            {
                "search_word": task.search_word,
                "search_engine": task.search_engine,
                "ua": USER_AGENT,
                "job_id": job.id
            }
            for job, task in jobs
        ]

        # デバッグ用にペイロードを表示
        for payload in sqs_payloads:
            logger.info(payload)
            # SQS送信ロジックをここに追加可能

        return {"statusCode": 200, "body": f"Successfully processed {len(sqs_payloads)} jobs."}

    except Exception as e:
        logger.error(f"Error: {e}")
        return {"statusCode": 500, "body": "An error occurred"}

    finally:
        session.close()