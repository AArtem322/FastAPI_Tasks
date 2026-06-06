from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    is_done: Mapped[bool] = mapped_column(default=False)
