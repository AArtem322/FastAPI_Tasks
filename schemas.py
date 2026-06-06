from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    title: str


class TaskRead(BaseModel):
    id: int
    title: str
    is_done: bool
    model_config = ConfigDict(from_attributes=True)


class TaskUpdate(BaseModel):
    title: str | None = None
    is_done: bool | None = None
