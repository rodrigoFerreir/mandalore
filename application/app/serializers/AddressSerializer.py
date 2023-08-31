from app.models import Address


class AddressSerializer():

    def __init__(self, data_query: Address) -> None:
        self.data_query = data_query
        self.data = self.__representation()

    def __representation(self) -> dict:
        if self.data_query:
            return {
                'id': self.data_query.id,
                'street': self.data_query.street,
                'number': self.data_query.number,
                'complement': self.data_query.complement,
                'neighborhood': self.data_query.neighborhood,
                'zip_code': self.data_query.neighborhood,
                'city': self.data_query.city,
                'state': self.data_query.state,
                'country': self.data_query.country,
                'created_at': self.data_query.created_at,
                'updated_at': self.data_query.updated_at,
                'username_create': self.data_query.username_create,
                'username_update': self.data_query.username_update,
            }
        else:
            return {}