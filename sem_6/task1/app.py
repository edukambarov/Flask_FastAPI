from fastapi import FastAPI
import uvicorn
from sem_6.task1.db import database
from sem_6.task1.router import router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(router, tags=["users"])

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='localhost',
        port=8000,
        reload=True)

