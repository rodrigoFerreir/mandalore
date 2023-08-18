from typing import List
from . import BaseRepository, ProductCategory


class ProductCategoryRepository(BaseRepository):

    @classmethod
    def create(cls, name: str) -> None:
        return ProductCategory.objects.create(name=name)

    @classmethod
    def get(cls) -> List[ProductCategory]:
        return ProductCategory.objects.all().order_by("id")

    @classmethod
    def get_by_name(cls, name: str) -> ProductCategory:
        return ProductCategory.objects.get(name=name)

    @classmethod
    def update(cls, _id: int, name: str) -> None:
        ProductCategory.objects.filter(id=_id).update(name=name)

    @classmethod
    def delete(cls, _id: int) -> None:
        ProductCategory.objects.get(id=_id).delete()
