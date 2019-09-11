from config import PER_PAGE
from collections import namedtuple
from tortoise import QuerySet

OrderPage = namedtuple('OrderPage', 'order page per')


async def order_page_params(order: str = None, page: int = 1, per: int = PER_PAGE):
    page = page - 1
    if page < 0:
        page = 0
    return OrderPage(order, page, per)


def build_with_order_page(query: QuerySet, order_page: OrderPage):
    if order_page.order:
        query = query.order_by(order_page.order)
    return query.offset(order_page.page * order_page.per).limit(order_page.per)


def render(data, code=0, msg=None):
    return {'code': code, 'msg': msg, 'data': data}


def success(data):
    return render(data)
