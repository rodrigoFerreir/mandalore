from . import *
from app.models import Contact


class ContactSerializer():

    def __init__(self, data_query: Contact) -> None:
        self.data_query = data_query
        self.data = self.__representation()

    def __representation(self) -> dict:
        return {
            "id": self.data_query.id,
            "email": self.data_query.email,
            "phone_number": self.data_query.phone_number,
        }
