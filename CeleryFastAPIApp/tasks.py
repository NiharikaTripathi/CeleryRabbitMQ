from CeleryFastAPIApp.celery_app import celery_app
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")  # Ensure MongoDB is running at this address
db = client["celery_tasks_db"]
tasks_collection = db["tasks"]

# Task to add numbers
@celery_app.task(bind=True)
def add_task_to_queue(self, a: int, b: int):
    result = a + b
    return result

# Function to check task status and result
def get_task_status(task_id: str):
    task_result = celery_app.AsyncResult(task_id)
    if task_result.state == "SUCCESS":
        return {"task_id": task_id, "status": task_result.state, "result": task_result.result}
    else:
        return {"task_id": task_id, "status": task_result.state}
