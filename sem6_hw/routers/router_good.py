from fastapi import APIRouter
from sem6_hw.dbs.db import database, goods
from sem6_hw.models.goods import Good, GoodIn

router_good = APIRouter()

@router_good.get('/goods/', response_model=list[Good])
async def get_goods():
    goods_ = goods.select()
    return await database.fetch_all(goods_)

@router_good.get("/goods/{good_id}", response_model=Good)
async def read_good(id: int):
    query = goods.select().where(goods.c.good_id == id)
    return await database.fetch_one(query)


@router_good.post('/goods/', response_model=Good)
async def add_good(good: GoodIn):
    query = goods.insert().values(**good.dict())
    last_record_id = await database.execute(query)
    return {**good.dict(), "good_id": last_record_id}

@router_good.put("/goods/{good_id}", response_model=Good)
async def update_good(id: int, new_good: GoodIn):
    query = goods.update().where(goods.c.good_id == id).values(**new_good.dict())
    await database.execute(query)
    return {**new_good.dict(), "good_id": id}

@router_good.delete("/goods/{good_id}")
async def delete_good(id: int):
    query = goods.delete().where(goods.c.good_id == id)
    await database.execute(query)
    return {'message': 'Good deleted'}
