from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()


@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks() -> list[task_schema.Task]:
    return [task_schema.Task(id=1, title="1つ目のTODOタスク")]


@router.post("/tasks")
async def create_task() -> None:
    pass


@router.put("/tasks/{task_id}")
async def update_task() -> None:
    pass


@router.delete("/tasks/{task_id}")
async def delete_task() -> None:
    pass
