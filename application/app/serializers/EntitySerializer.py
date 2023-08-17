from . import *
from app.models import Entity


class EntitySerializer():

    def __init__(self, data_query: Entity) -> None:
        self.data_query = data_query
        self.data = self.__representation()

    def __representation(self) -> dict:
        return {
            "name": self.data_query.name,
            "cpf_cnpj": self.data_query.cpf_cnpj,
            "category": self.data_query.category.name
        }