

from typing import List
from . import BaseRepository, EntityCategory


class EntityCategoryRepository(BaseRepository):

    @classmethod
    def create(cls, name: str) -> None:
        return EntityCategory.objects.create(name=name)

    @classmethod
    def get(cls) -> List[EntityCategory]:
        return EntityCategory.objects.all().order_by("id")

    @classmethod
    def get_by_name(cls, name: str) -> List[EntityCategory]:
        category = EntityCategory.objects.get(name=name)
        return category

    @classmethod
    def update(cls, _id: int, name: str) -> None:
        EntityCategory.objects.filter(id=_id).update(name=name)

    @classmethod
    def delete(cls, _id: int) -> None:
        EntityCategory.objects.get(id=_id).delete()
