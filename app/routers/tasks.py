from fastapi import APIRouter, HTTPException
from app.models.models import Task
from app.db.db import fake_db
import uuid

router = APIRouter()

@router.post('/task_create')
def create_task(task: Task):
    task_id = str(uuid.uuid4())
    fake_db[task_id] = task
    return {"id": task_id, "task": task}

@router.get('/task_all')
def read_all_tasks():
    return {"tasks": list(fake_db.values())}

@router.get('/task/{id}')
def read_task(id: str):
    task = fake_db.get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put('/task/{id}')
def update_task(id: str, updated_task: Task):
    if id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")
    fake_db[id] = updated_task
    return {"message": "Task updated", "task": updated_task}

@router.delete('/task/{id}')
def delete_task(id: str):
    if id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")
    deleted = fake_db.pop(id)
    return {"message": "Task deleted", "task": deleted}

