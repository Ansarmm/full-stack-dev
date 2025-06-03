from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []
current_id = 0

class TaskCreate(BaseModel):
    desc: str

class Task(BaseModel):
    desc: str
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

@app.post("/tasks/", response_model = Task)
async def post_task(task: TaskCreate):
    global current_id
    current_id += 1
    new_task = Task(id=current_id, desc=task.desc)
    tasks.append(new_task)
    return new_task

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

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: TaskCreate):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = Task(id=task.id, desc=updated_task.desc)
            return tasks[index]
    raise HTTPException(status_code=404, detail="Task not found")