from . import *
from app.models import ItemOrder


class ItemOrderSerializer():

    def __init__(self, data_query: ItemOrder = None) -> None:
        self.data_query = data_query
        self.data = self.__representation()

    def __representation(self) -> dict:
        if self.data_query:
            return {
                "id":self.data_query.id,
                "products": ProductSerializer(self.data_query.product).data,
                "qtd": self.data_query.amount,
                "total_value": self.data_query.total_value
            }
        else:
            return {}