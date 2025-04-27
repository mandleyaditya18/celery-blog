from celery import Celery

app = Celery("my_celery_app", broker="redis://localhost:6379/0")


# Define a simple task
@app.task
def add(x, y):
    return x + y
