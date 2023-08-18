from typing import List
from . import BaseRepository, Entity, EntityCategory


class EntityRepository(BaseRepository):

    @classmethod
    def create(cls, name: str, cpf_cnpj: str, category: EntityCategory) -> None:
        return Entity.objects.create(name=name, cpf_cnpj=cpf_cnpj, category=category)

    @classmethod
    def get(cls) -> List[Entity]:
        return Entity.objects.all().order_by("id")

    @classmethod
    def get_by_name(cls, name: str) -> List[Entity]:
        return Entity.objects.filter(name=name).order_by("id")

    @classmethod
    def get_by_cpf_cnpj(cls, cpf_cnpj: str) -> List[Entity]:
        return Entity.objects.filter(cpf_cnpj=cpf_cnpj).order_by("id")

    @classmethod
    def update(cls, _id: int, name: str, cpf_cnpj: str, category: EntityCategory) -> None:
        Entity.objects.filter(id=_id).update(
            name=name, cpf_cnpj=cpf_cnpj, category=category)

    @classmethod
    def delete(cls, _id: int) -> None:
        Entity.objects.get(id=_id).delete()
