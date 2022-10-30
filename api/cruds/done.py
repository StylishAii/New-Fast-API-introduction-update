from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model


async def get_done(db: AsyncSession, task_id: int) -> None | task_model.Done:
    result: Result = await db.execute(
        select(task_model.Done).filter(task_model.Done.id == task_id)
    )
    done: None | tuple[task_model.Done] = result.first()
    if done is None:
        return None
    # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
    return done[0]


async def create_done(db: AsyncSession, task_id: int) -> task_model.Done:
    done = task_model.Done(id=task_id)
    db.add(done)
    await db.commit()
    await db.refresh(done)
    return done


async def delete_done(db: AsyncSession, original: task_model.Done) -> None:
    await db.delete(original)
    await db.commit()
