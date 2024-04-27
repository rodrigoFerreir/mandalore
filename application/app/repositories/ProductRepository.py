from typing import List
from . import BaseRepository, Product, ProductCategory


class ProductRepository(BaseRepository):

    @classmethod
    def create(cls, name: str, price: float, category: ProductCategory, url_image: str) -> None:
        return Product.objects.create(name=name, price=price, category=category, url_image=url_image)

    @classmethod
    def get(cls) -> List[Product]:
        return Product.objects.all().order_by("id")

    @classmethod
    def get_by_id(cls, _id: str) -> Product:
        return Product.objects.get(id=_id)

    @classmethod
    def get_by_name(cls, name: str) -> List[Product]:
        return Product.objects.filter(name=name).order_by("id")

    @classmethod
    def update(cls, _id: int, name: str, price: float, category: ProductCategory, url_image: str) -> None:
        Product.objects.filter(id=_id).update(
            name=name, price=price, category=category, url_image=url_image)

    @classmethod
    def delete(cls, _id: int) -> None:
        Product.objects.get(id=_id).delete()
