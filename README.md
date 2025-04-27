# 🥬 Celery Blog – Part 1: Minimal Celery App

This branch contains the code for **Part 1** of the blog series:
**“Getting Started with Celery: Background Task Processing Made Simple”**

<!-- 📖 Read the blog post: [Part 1 – Minimal Celery Setup](https://your-blog.com/part-1) -->

---

## 🧾 What's in this branch?

A super minimal Celery app with:

- A single task (`add(x, y)`)
- Redis as the message broker
- Everything needed to run and test it locally

---

## 🚀 Getting Started

### 1. Clone the repo & switch to this branch

### 2. Set up a virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

Make sure you have Redis running on `localhost:6379`.

---

## 🔨 Running the Celery worker

In one terminal:

```
celery -A tasks worker --loglevel=info
```

---

## 📬 Sending a Task

Open another terminal (while the worker is running):

```
python
```

Then:

```python
from tasks import add
add.delay(2, 3)
```

You should see the result printed in the worker terminal!

---

## 🧾 Files in this branch

- `tasks.py` – defines the Celery app and one example task
- `requirements.txt` – dependency list (Celery + Redis)

---

<!-- ## ⏭️ What's Next?

In [Part 2](https://your-blog.com/part-2), we’ll explore how to run periodic tasks with Celery Beat. Stay tuned! -->
