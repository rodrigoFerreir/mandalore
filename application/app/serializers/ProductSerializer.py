from . import *
from app.models import Product


class ProductSerializer():

    def __init__(self, data_query: Product) -> None:
        self.data_query = data_query
        self.data = self.__representation()

    def __representation(self) -> dict:
        return {
            "id":self.data_query.id,
            "name": self.data_query.name,
            "price": self.data_query.price,
            "category": self.data_query.category.name
        }
