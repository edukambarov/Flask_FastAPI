# Задание №2
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, HTTPException
import logging
from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Genre(BaseModel):
    id: int
    name: Optional[str] = None


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: Genre


movies = [Movie(id=0,
                title='Titanic',
                description='Legendary catastroph drama from James Cameron starring Leonardo Di Caprio',
                genre=Genre(id=0, name='drama')),
          Movie(id=1,
                title='Terminator',
                description='Legendary action from James Cameron starring Arnold Schwarznegger',
                genre=Genre(id=1, name='action')),
          Movie(id=2,
                title='Операция "Ы"',
                description='Classic Soviet comedy from Leonid Gaidai',
                genre=Genre(id=2, name='comedy')),
          Movie(id=3,
                title='Green Mile',
                description='Legendary drama starring Tom Hanks',
                genre=Genre(id=0, name='drama')),
          ]


@app.get('/movies/', response_model=list[Movie])
async def get_movies(genre_id: int = None):
    if genre_id is not None:
        return [movie for movie in movies if movie.genre.id == genre_id]
    return movies



if __name__ == '__main__':
    uvicorn.run("task2:app",
                host='localhost',
                port=8000,
                reload=True)
