from fastapi import FastAPI, BackgroundTasks
from CeleryFastAPIApp.tasks import add_task_to_queue, get_task_status
from pydantic import BaseModel

app = FastAPI()

# Data model for the task
class TaskInput(BaseModel):
    a: int
    b: int

# Endpoint to trigger a task
@app.post("/add")
async def add_numbers(task_input: TaskInput, background_tasks: BackgroundTasks):
    task_id = add_task_to_queue.delay(task_input.a, task_input.b)  # Adding to Celery queue
    return {"task_id": task_id.id}

# Endpoint to get the status of a task
@app.get("/status/{task_id}")
async def task_status(task_id: str):
    status = get_task_status(task_id)
    return status
