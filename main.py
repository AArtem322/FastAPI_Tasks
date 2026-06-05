import os

from dotenv import load_dotenv
from fastapi import FastAPI

from fastapi.templating import Jinja2Templates

from database import engine, Base
from routers import tasks, pages
from fastapi.staticfiles import StaticFiles

load_dotenv()
app = FastAPI()
database_url = os.getenv('DATABASE_URL')

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(tasks.router)
app.include_router(pages.router)
Base.metadata.create_all(engine)
