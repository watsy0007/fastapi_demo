from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel, Schema
from db import Event
from utils import order_page_params, OrderPage, build_with_order_page, success
from response_model import Default

router = APIRouter()


class EventModel(BaseModel):
    name: str = Schema(None, title='名称', description='事件的名称', min_length=4, max_length=128)
    id: int = None

    class Config:
        orm_mode = True


class CreateEvent(Default):
    data: EventModel


@router.get('/', response_model=Default, summary='获取所有事件', )
async def events(order_page: OrderPage = Depends(order_page_params)):
    """
    获取所有事件
    """
    result = await build_with_order_page(Event.all(), order_page)
    return result


@router.post('/', response_model=Default, summary='新建事件')
async def create(item: EventModel = Body(..., example={'name': 'new event'})):
    """
    新建事件
    """
    r: Event = await Event.create(**item.dict(skip_defaults=True))
    return success(EventModel.from_orm(r))