from typing import List
from . import BaseRepository, Product, ItemOrder


class ItemOrderRepository(BaseRepository):

    @classmethod
    def create(cls, product: Product, amount:int, total_value:float) -> None:
        return ItemOrder.objects.create(product=product, amount=amount, total_value=total_value)

    @classmethod
    def get(cls) -> List[ItemOrder]:
        return ItemOrder.objects.all().Itemorder_by("id")

    @classmethod
    def get_by_product_id(cls, product_id: int) -> List[ItemOrder]:
        return ItemOrder.objects.filter(product__id = product_id)

    @classmethod
    def update(cls, _id: int, product: Product, amount:int, total_value:float) -> None:
        ItemOrder.objects.filter(id=_id).update(product=product, amount=amount, total_value=total_value)

    @classmethod
    def delete(cls, _id: int) -> None:
        ItemOrder.objects.get(id=_id).delete()
