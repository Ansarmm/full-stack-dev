from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    name: str
    id: int


@app.get("/tasks/")
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
async def get_task_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks/")
async def post_task(task: Task):
    tasks.append(task)
    return {
        "message": "Task list",
        "task": task
    }

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            deleted = tasks.pop(index)
            return {
                "message": f"Task with id={task_id} deleted",
                "deleted_task": deleted
            }
    raise HTTPException(status_code=404, detail=f"Task with id={task_id} not found")

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task  
            return {
                "message": f"Task with id={task_id} updated",
                "task": updated_task
            }
    raise HTTPException(status_code=404, detail="Task not found")
