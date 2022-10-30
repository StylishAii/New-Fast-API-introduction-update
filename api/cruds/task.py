from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema


async def get_tasks_with_done(db: AsyncSession) -> list[task_schema.Task]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).outerjoin(task_model.Done)
        )
    )
    tasks = [
        task_schema.Task(title=title, id=id, done=done)
        for (id, title, done) in result.all()
    ]
    return tasks


async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_task(db: AsyncSession, task_id: int) -> None | task_model.Task:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: None | task_model.Task = result.first()
    if task is not None:
        # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
        return task[0]  # type: ignore
    return None


async def update_task(
    db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_schema.TaskCreateResponse:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original
