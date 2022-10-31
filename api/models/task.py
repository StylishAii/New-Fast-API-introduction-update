from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    done: bool = relationship("Done", back_populates="task")


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task: list[Task] = relationship("Task", back_populates="done")
