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
                "id": self.data_query.id,
                "date": self.data_query.date_order.strftime("%m/%d/%Y - %H:%M:%S"),
                "total_value_order": self.data_query.total_value_order,
                "status": self.data_query.get_status_order,
                "status_payment": self.data_query.get_status_payment,
                "entity_data": EntitySerializer(self.data_query.entity).data,
                "address": AddressSerializer(self.data_query.address).data if self.data_query.address else None, 
                "itens":[ItemOrderSerializer(item).data for item in self.data_query.itens_order.all()] if self.data_query else []
            }
        else:
            return {}