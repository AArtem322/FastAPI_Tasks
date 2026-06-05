
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Task
from schemas import TaskCreate, TaskUpdate


def get_all_tasks(db: Session):
    query = select(Task)
    tasks = db.scalars(query).all()
    return tasks

def create_task(db: Session, task_data: TaskCreate):
    task = Task(title=task_data.title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(db: Session, task_id: int):
    task = db.get(Task, task_id)
    return task

def update_task(db: Session, task: Task, task_data: TaskUpdate):
    update_data = task_data.model_dump(exclude_unset=True)
    for field,value in update_data.items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()

def toggle_task(db: Session, task: Task):
    task.is_done = not task.is_done
    db.commit()
    db.refresh(task)
    return task