from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from services import tasks as tasks_service

from database import get_db
from schemas import TaskRead, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
def index():
    return {"message": "Hello World"}


@router.get("/", response_model=list[TaskRead])
def get_tasks(db: Session = Depends(get_db)):
    tasks = tasks_service.get_all_tasks(db)
    return tasks


@router.post("/", response_model=TaskRead)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    task = tasks_service.create_task(db, task_data)
    return task


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = tasks_service.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    task = tasks_service.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = tasks_service.update_task(db, task, task_data)
    return update_data


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = tasks_service.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_service.delete_task(db, task)
    return {"message": "Task deleted"}


@router.patch("/{task_id}/toggle", response_model=TaskRead)
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    task = tasks_service.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = tasks_service.toggle_task(db, task)
    return updated_task
