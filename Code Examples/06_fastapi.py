"""
Build a small Task (TODO) API with FastAPI. Do not use a database; store everything in a global variable.
Requirements
Each task has: id (int), title (str), completed (bool), created_at (ISO-8601 string).

Endpoints:

POST /tasks - create a task from {title}; return the created task.
GET /tasks - list all tasks.
GET /tasks/{id} - get one task by id.
PATCH /tasks/{id} - update title and/or completed.
DELETE /tasks/{id} - delete a task (204 on success).

Use a global in-memory store (e.g., dict or list). IDs must be unique and auto-incrementing.
Return proper HTTP status codes and errors (404 if a task doesn't exist).

"""
# Install fastapi
# pip install "fastapi[standard]"
# pip install "uvicorn[standard]"
# To run the app, use: uvicorn 06_fastapi:app --reload


from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime, timezone

app = FastAPI(
    title="In-Memory Task API", 
    version="1.0",
    docs_url="/")

# ------------------------------
# Db simulation
# ------------------------------
_TASKS: Dict[int, dict] = {}


# ------------------------------
# Schemas
# ------------------------------
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    completed: Optional[bool] = None


class Task(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: str


# ------------------------------
# Helpers
# ------------------------------
def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def _get_or_404(task_id: int) -> dict:
    task = _TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# ------------------------------
# Routes
# ------------------------------
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    next_id = (max(_TASKS.keys()) + 1) if _TASKS else 1
    task = {
        "id": next_id,
        "title": payload.title,
        "completed": False,
        "created_at": _now_iso(),
    }
    _TASKS[next_id] = task
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(_TASKS.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    return _get_or_404(task_id)


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate):
    task = _get_or_404(task_id)
    if payload.title is not None:
        task["title"] = payload.title
    if payload.completed is not None:
        task["completed"] = payload.completed
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    _get_or_404(task_id)  # ensure exists
    del _TASKS[task_id]
    return None

# To run the app, use: uvicorn 6_fastapi:app --reload
