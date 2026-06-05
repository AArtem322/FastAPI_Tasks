from fastapi import APIRouter, HTTPException, Request, Form, Depends
from sqlalchemy.orm import Session


from database import get_db

from schemas import TaskRead, TaskCreate, TaskUpdate
from fastapi.responses import RedirectResponse
from services import tasks as tasks_service
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/pages", tags=["pages"])

templates = Jinja2Templates(directory="templates")


@router.get("/tasks")
def list_pages(request: Request, db: Session = Depends(get_db)):
    tasks = tasks_service.get_all_tasks(db)
    task_data = []
    for task in tasks:
        task_data.append(
            {"id": task.id, "title": task.title, "is_done": task.is_done}
        )

    return templates.TemplateResponse(request, "tasks.html", {"request": request, "tasks": task_data})


@router.get("/tasks/create")
def create_task_page(request: Request):
    return templates.TemplateResponse(request, "task_create.html", {"request": request})


@router.post("/tasks/create", response_model=TaskRead)
def create_task_from_form(title: str = Form(...), db: Session = Depends(get_db)):
        task = TaskCreate(title=title)
        tasks_service.create_task(db, task)
        return RedirectResponse(url="/pages/tasks", status_code=303)


@router.get("/tasks/{task_id}/edit")
def edit_task_page(request: Request, task_id: int, db: Session = Depends(get_db)):
        task = tasks_service.get_task_by_id(db, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        task_data = {"id": task.id, "title": task.title, "is_done": task.is_done}
        return templates.TemplateResponse(request, "task_edit.html", {"request": request, "task": task_data})


@router.post("/tasks/{task_id}/edit", response_model=TaskRead)
def edit_task_from_form(task_id: int, title: str = Form(...), is_done: bool = Form(False), db: Session = Depends(get_db)):
        task = tasks_service.get_task_by_id(db, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        task_data = TaskUpdate(title=title, is_done=is_done)
        tasks_service.update_task(db, task, task_data)
        return RedirectResponse(url="/pages/tasks", status_code=303)


@router.post("/tasks/{task_id}/delete")
def delete_task_page(task_id: int, db: Session = Depends(get_db)):
        task = tasks_service.get_task_by_id(db, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        tasks_service.delete_task(db, task)
        return RedirectResponse(url="/pages/tasks", status_code=303)
