from . import *
from app.models import Entity, Address
from typing import List
from .AddressSerializer import AddressSerializer
from app.models import Address


class TransformListSerializer(serializers.ListSerializer):
    def to_representation(self, instances: List[Entity]):
        return [{
            "name": instance.name,
            "cpf_cnpj": instance.cpf_cnpj,
            "category": instance.category.name,
            "address": self.__get_address_entities(instance.id)
        } for instance in instances]


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity

    def __get_address_entities(self, entity_id: int) -> List[Address]:
        data = Address.objects.filter(entity__id=entity_id).order_by('id')
        serializer = AddressSerializer(data=data, many=True)
        print(serializer.data)
        return serializer.data

    def to_representation(self, instance: Entity):
        address = self.__get_address_entities(instance.id)
        return {
            "name": instance.name,
            "cpf_cnpj": instance.cpf_cnpj,
            "category": instance.category.name,
            "address": address
        }
