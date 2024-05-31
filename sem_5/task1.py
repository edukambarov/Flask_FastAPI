# Задание №1
# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.


import uvicorn
from fastapi import FastAPI, HTTPException
import logging
from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[bool] = False


tasks = []

@app.get('/task/', response_model=list[Task])
async def get_tasks():
    return [task for task in tasks if not task.status]

@app.get('/task/{id}', response_model=Task)
async def get_task(id: int):
    task = [task for task in tasks if task.id == id]
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task[0]


@app.post('/task/', response_model=Task)
async def create_task(task: Task):
    if [t for t in tasks if t.id == task.id]:
        raise HTTPException(status_code=409, detail="Task already exits")
    tasks.append(task)
    return task

@app.put('/task/', response_model=Task)
async def update_task(task: Task):
    for ind in range(len(tasks)):
        if tasks[ind].id == task.id:
            tasks[ind] = task
            return tasks[ind]
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete('/task/', response_model=Task)
async def delete_task(id: int):
    for ind in range(len(tasks)):
        if tasks[ind].id == id:
            tasks.pop(ind)
            return {'message': 'Task deleted'}
    raise HTTPException(status_code=404, detail="Task not found")




if __name__ == '__main__':
    uvicorn.run("task1:app",
                host='localhost',
                port=8000,
                reload=True)

