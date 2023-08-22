from typing import List
from . import BaseRepository, Order,  Entity, Address


class OrderRepository(BaseRepository):

    @classmethod
    def create(cls, entity:Entity, address:Address) -> Order:
        return Order.objects.create(entity = entity, address=address)

    @classmethod
    def get(cls) -> List[Order]:
        return Order.objects.all().order_by("id")

    @classmethod
    def get_by_date_order(cls, date_order: str) -> Order:
        return Order.objects.get(date_order=date_order)

    @classmethod
    def update(cls, _id: int, name: str) -> None:
        Order.objects.filter(id=_id).update(name=name)

    @classmethod
    def delete(cls, _id: int) -> None:
        Order.objects.get(id=_id).delete()
