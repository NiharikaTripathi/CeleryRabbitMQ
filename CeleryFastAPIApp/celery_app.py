from celery import Celery

# Configuring Celery to use RabbitMQ for both the broker and the backend
celery_app = Celery(
    "worker",
    broker="pyamqp://guest:guest@localhost//",  # RabbitMQ broker
    backend="rpc://",                           # RabbitMQ backend
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
def import_tasks():
    import CeleryFastAPIApp.tasks

import_tasks()

celery_app.conf.task_default_queue = "celeryQueue"