# Задание
#
# Необходимо создать API для управления списком задач.
# Каждая задача должна содержать заголовок и описание.
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
#
# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
#
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
# Для этого использовать библиотеку Pydantic.

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

@app.get('/tasks/', response_model=list[Task])
async def get_tasks():
    return [task for task in tasks if not task.status]

@app.get('/tasks/{id}', response_model=Task)
async def get_task(id: int):
    task = [task for task in tasks if task.id == id]
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task[0]


@app.post('/tasks/', response_model=Task)
async def create_task(task: Task):
    if [t for t in tasks if t.id == task.id]:
        raise HTTPException(status_code=409, detail="Task already exits")
    tasks.append(task)
    return task

@app.put('/tasks/{id}', response_model=Task)
async def update_task(id: int, task: Task):
    for ind in range(len(tasks)):
        if tasks[ind].id == id:
            tasks[ind] = task
            return tasks[ind]
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete('/tasks/{id}', response_model=Task)
async def delete_task(id: int):
    for ind in range(len(tasks)):
        if tasks[ind].id == id:
            tasks.pop(ind)
            return {'message': 'Task deleted'}
    raise HTTPException(status_code=404, detail="Task not found")




if __name__ == '__main__':
    uvicorn.run("hw:app",
                host='localhost',
                port=8000,
                reload=True)

