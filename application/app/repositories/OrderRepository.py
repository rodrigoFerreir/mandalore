from typing import List
from . import BaseRepository, Order


class OrderRepository(BaseRepository):

    @classmethod
    def create(cls, name: str) -> None:
        return Order.objects.create(name=name)

    @classmethod
    def get(cls) -> List[Order]:
        return Order.objects.all().order_by("id")

    @classmethod
    def get_by_name(cls, name: str) -> Order:
        return Order.objects.get(name=name)

    @classmethod
    def update(cls, _id: int, name: str) -> None:
        Order.objects.filter(id=_id).update(name=name)

    @classmethod
    def delete(cls, _id: int) -> None:
        Order.objects.get(id=_id).delete()
