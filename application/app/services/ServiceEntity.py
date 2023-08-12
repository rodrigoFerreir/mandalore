from app.serializer.EntitySerializer import EntitySerializer
from . import *


class ServiceEntity(BaseService):

    def __init__(self, data=dict) -> None:
        self.data_entity = data
        self.data_address = data.get('address')
        self.data_contact = data.get('contact')
        self.repository = EntityRepository()
        self.category_repository = EntityCategoryRepository()

    def create(self):

        try:
            self.repository.create(
                name=self.data_entity['name'],
                cpf_cnpj=self.data_entity['identity'],
                category=self.category_repository.get_by_name(self.data_entity["category"]),
            )
        except Exception as error:
            raise Exception(f'Error on create Organization {error}')
        else:
            return {
                'message': 'Entidade criada com sucesso!',
            }

    def get(self):
        try:
            _result: list = []
            data_query = self.repository.get()
            serializer = EntitySerializer(data=data_query, many=True)
            _result = serializer.to_representation(data_query)
            # for item in data_query:
            #     item_address = Address.objects.filter(organization=item.id)
            #     item_contact = Contact.objects.filter(organization=item.id)
            #     _result.append({
            #         "_id": item.id,
            #         "name": item.name,
            #         "cpf_cnpj": item.identity,
            #         "type": item._type,
            #         "addresses": [{
            #             'id': item.id,
            #             'street': item.street,
            #             'number': item.number,
            #             'complement': item.complement,
            #             'neighborhood': item.neighborhood,
            #             'zip_code': item.neighborhood,
            #             'city': item.city,
            #             'state': item.state,
            #             'country': item.country,
            #             'created_at': item.created_at,
            #             'updated_at': item.updated_at,
            #             'username_create': item.username_create,
            #             'username_update': item.username_update,
            #         } for item in item_address],
            #         "contacts": [{
            #             "id": item.id,
            #             "email": item.email,
            #             "phone_number": item.phone_number,
            #         } for item in item_contact]

            #     })
        except Exception as error:
            raise Exception(f'Erro on get Entities {error}')
        else:
            return _result

    def update(self, data_request: dict):
        try:
            data_request = data_request['org']
            if item_organization := Organization.objects.filter(id=data_request.get('id')).last():
                item_organization.name = data_request.get("name", item_organization.name)
                item_organization.identity = data_request.get("identity", item_organization.identity)
                item_organization._type = data_request.get("type", item_organization._type)
                Address.objects.filter(organization=item_organization).update(
                    street=data_request.get('address').get('street'),
                    number=data_request.get('address').get('number'),
                    complement=data_request.get('address').get('complement'),
                    neighborhood=data_request.get('address').get('neighborhood'),
                    zip_code=data_request.get('address').get('zip_code'),
                    city=data_request.get('address').get('city'),
                    state=data_request.get('address').get('state'),
                    country=data_request.get('address').get('country'),
                )
                Contact.objects.filter(organization=item_organization).update(
                    email=data_request.get('contact').get('email'),
                    phone_number=data_request.get('contact').get('phone_number'),
                )
        except Exception as error:
            raise Exception(f'Erro on update Organization {error}')
        else:
            return self.get(item_organization.id)

    def delete(self, id: int = None):
        try:
            if item_organization := Organization.objects.filter(id=id).last():
                item_organization.delete()
        except Exception as error:
            raise Exception(f'Erro on update Organization {error}')
        else:
            return "Item deletado!"
