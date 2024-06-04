from fastapi import APIRouter, HTTPException
from sem6_hw.dbs.db import database, users
from sem6_hw.models.users import User, UserIn

router_user = APIRouter()

@router_user.get('/users/', response_model=list[User])
async def get_users():
    users_ = users.select()
    return await database.fetch_all(users_)


@router_user.get("/users/{user_id}", response_model=User)
async def read_user(id: int):
    query = users.select().where(users.c.user_id == id)
    if not query:
        raise HTTPException(status_code=404, detail="User not found")
    return await database.fetch_one(query)


@router_user.post('/users/', response_model=User)
async def add_user(user: UserIn):
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "user_id": last_record_id}

@router_user.put("/users/{user_id}", response_model=User)
async def update_user(id: int, new_user: UserIn):
    query = users.update().where(users.c.user_id == id).values(**new_user.dict())
    if not query:
        raise HTTPException(status_code=404, detail="User not found")
    await database.execute(query)
    return {**new_user.dict(), "user_id": id}


@router_user.delete("/users/{user_id}")
async def delete_user(id: int):
    query = users.delete().where(users.c.user_id == id)
    if not query:
        raise HTTPException(status_code=404, detail="User not found")
    await database.execute(query)
    return {'message': 'User deleted'}


