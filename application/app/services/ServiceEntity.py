from app.serializers import *
from . import *


class ServiceEntity(BaseService):

    def __init__(self, data=dict) -> None:
        self.data_entity = data
        self.data_address = data.get('address')
        self.data_contact = data.get('contact')
        self.repository = EntityRepository()
        self.category_repository = EntityCategoryRepository()
        self.address_repository = AddressRepository()
        self.contact_repository = ContactRepository()

    def create(self):

        try:
            instance_entity = self.repository.create(
                name=self.data_entity['name'],
                cpf_cnpj=self.data_entity['cpf_cnpj'],
                category=self.category_repository.get_by_name(self.data_entity["category"]),
            )
            self.address_repository.create(
                street=self.data_address['street'],
                number=self.data_address['number'],
                complement=self.data_address['complement'],
                neighborhood=self.data_address['neighborhood'],
                zip_code=self.data_address['zip_code'],
                city=self.data_address['city'],
                state=self.data_address['state'],
                country=self.data_address['country'],
                entity=instance_entity,
            )
            self.contact_repository.create(
                email=self.data_contact["email"],
                phone_number=self.data_contact["phone_number"],
                entity=instance_entity,

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
            for item in data_query:
                data = EntitySerializer(item).data
                data['addresses'] = [AddressSerializer(a).data for a in self.address_repository.get_by_entity(item.id)]
                data['contacts'] = [ContactSerializer(c).data for c in self.contact_repository.get_by_entity(item.id)]
                _result.append(data)
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
