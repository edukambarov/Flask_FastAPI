from fastapi import APIRouter, HTTPException
from sem6_hw.dbs.db import database, orders, users, goods
# from sem6_hw.models.users import User, UserIn
# from sem6_hw.models.goods import Good, GoodIn
from sem6_hw.models.orders import OrderIn, Order

router_order = APIRouter()


# @router_order.get('/orders/', response_model=list[Order])
# async def get_all_orders():
#     all_orders = orders.select()
#     return await database.fetch_all(all_orders)

# @router_order.get('/orders/', response_model=list[Order])
# async def get_inactive_orders():
#     inactive_orders = orders.select().where(orders.c.status is False)
#     return await database.fetch_all(inactive_orders)

@router_order.get('/orders/', response_model=list[Order])
async def get_active_orders():
    active_orders = orders.select().where(orders.c.status)
    return await database.fetch_all(active_orders)


@router_order.get("/orders/{order_id}", response_model=Order)
async def read_order(id: int):
    query = orders.select().where(orders.c.order_id == id)
    if not query:
        raise HTTPException(status_code=404, detail="Order not found")
    return await database.fetch_one(query)


@router_order.post('/orders/', response_model=Order)
async def add_order(order: OrderIn):
    query = orders.insert().values(**order.dict())
    last_record_id = await database.execute(query)
    return {**order.dict(), "order_id": last_record_id}


@router_order.put("/orders/{order_id}", response_model=Order)
async def update_order(id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.order_id == id).values(**new_order.dict())
    if not query:
        raise HTTPException(status_code=404, detail="Order not found")
    await database.execute(query)
    return {**new_order.dict(), "order_id": id}


# @router_order.delete("/orders/{order_id}")
# async def delete_order(id: int):
#     query = orders.delete().where(orders.c.order_id == id).values()
#     if not query:
#         raise HTTPException(status_code=404, detail="Order not found")
#     await database.execute(query)
#     return {'message': 'Order deleted'}


@router_order.delete("/orders/{order_id}")
async def soft_delete_order(id: int):
    query = orders.update().where(orders.c.order_id == id).values(status=False)
    if not query:
        raise HTTPException(status_code=404, detail="Order not found")
    await database.execute(query)
    return {'message': 'Order inactivated'}
