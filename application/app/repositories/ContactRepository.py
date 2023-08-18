from typing import List
from . import BaseRepository, Contact, Entity


class ContactRepository(BaseRepository):

    @classmethod
    def create(cls, email: str, phone_number: str, entity: Entity) -> None:
        return Contact.objects.create(email=email, phone_number=phone_number, entity=entity)

    @classmethod
    def get(cls) -> List[Contact]:
        return Contact.objects.all().order_by("id")

    @classmethod
    def get_by_entity(cls, entity_id: int) -> List[Contact]:
        return Contact.objects.filter(entity_id=entity_id).order_by("id")

    @classmethod
    def update(cls, _id: int, email: str, phone_number: str, entity: Entity) -> None:
        Contact.objects.filter(id=_id).update(
            email=email, phone_number=phone_number, entity=entity)

    @classmethod
    def delete(cls, _id: int) -> None:
        Contact.objects.get(id=_id).delete()
