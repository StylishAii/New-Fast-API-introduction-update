from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int) -> None:
    return None


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int) -> None:
    return None
