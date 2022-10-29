from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()


@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks() -> list[task_schema.Task]:
    return [task_schema.Task(id=1, title="1つ目のTODOタスク")]


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(
    task_body: task_schema.TaskCreate,
) -> task_schema.TaskCreateResponse:
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(
    task_id: int, task_body: task_schema.TaskCreate
) -> task_schema.TaskCreateResponse:
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int) -> None:
    return None
