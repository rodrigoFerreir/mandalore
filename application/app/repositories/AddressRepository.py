from typing import List
from . import BaseRepository, Address, Entity


class AddressRepository(BaseRepository):

    @classmethod
    def create(
        cls,
        street: str,
        number: str,
        complement: str,
        neighborhood: str,
        zip_code: str,
        city: str,
        state: str,
        country: str,
        entity: Entity
    ) -> Address:
        return Address.objects.create(
            street=street,
            number=number,
            complement=complement,
            neighborhood=neighborhood,
            zip_code=zip_code,
            city=city,
            state=state,
            country=country,
            entity=entity
        )

    @classmethod
    def get(cls) -> List[Address]:
        return Address.objects.all().order_by("id")

    @classmethod
    def get_or_create(
        cls,
        street: str,
        number: str,
        complement: str,
        neighborhood: str,
        zip_code: str,
        city: str,
        state: str,
        country: str,
        entity: Entity
    ) -> Address:
        if address := Address.objects.filter(street=street, 
                                            number=number,
                                            complement=complement, 
                                            neighborhood=neighborhood, 
                                            zip_code=zip_code,
                                            city=city,
                                            state=state,
                                            country=country,
                                            entity=entity).last():
            return address
        else:
            return Address.objects.create(
                street=street,
                number=number,
                complement=complement,
                neighborhood=neighborhood,
                zip_code=zip_code,
                city=city,
                state=state,
                country=country,
                entity=entity
            )

    @classmethod
    def get_by_entity(cls, entity_id: int) -> List[Address]:
        return Address.objects.filter(entity__id=entity_id).order_by("id")

    @classmethod
    def update(
        cls,
        _id: int,
        street: str,
        number: str,
        complement: str,
        neighborhood: str,
        zip_code: str,
        city: str,
        state: str,
        country: str,
        entity: Entity
    ) -> None:
        Address.objects.filter(id=_id).update(
            street=street,
            number=number,
            complement=complement,
            neighborhood=neighborhood,
            zip_code=zip_code,
            city=city,
            state=state,
            country=country,
            entity=entity
        )

    @classmethod
    def delete(cls, _id: int) -> None:
        Address.objects.get(id=_id).delete()
