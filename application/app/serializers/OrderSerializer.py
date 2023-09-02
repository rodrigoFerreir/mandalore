from . import *
from app.models import Order


class OrderSerializer():

    def __init__(self, data_query: Order = None) -> None:
        self.data_query = data_query
        self.data = self.__representation()

    def __representation(self) -> dict:
        if self.data_query:
            self.data_query._calculate_total_value_order()
            return {
                "date": self.data_query.date_order.strftime("%m/%d/%Y - %H:%M:%S"),
                "total_value_order": self.data_query.total_value_order,
                "entity_data": EntitySerializer(self.data_query.entity).data,
                "address": AddressSerializer(self.data_query.entity.addresses.last()).data,
                "itens":[ItemOrderSerializer(item).data for item in self.data_query.itens_order.all()]
            }
        else:
            return {}