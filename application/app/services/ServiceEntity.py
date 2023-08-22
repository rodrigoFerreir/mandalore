from . import *


class ServiceEntity(BaseService):

    def __init__(self, data: dict = None) -> None:
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
                category=self.category_repository.get_by_name(
                    self.data_entity["category"]),
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
                data['addresses'] = [
                    AddressSerializer(a).data for a in item.addresses]
                data['contacts'] = [
                    ContactSerializer(c).data for c in item.contacts
                ]
                _result.append(data)
        except Exception as error:
            raise Exception(f'Erro on get Entities {error}')
        else:
            return _result

    def update(self):
        try:
            instance_entity = self.repository.update(
                _id=self.data_entity.get("id"),
                name=self.data_entity.get('name'),
                cpf_cnpj=self.data_entity.get('cpf_cnpj'),
                category=self.category_repository.get_by_name(
                    self.data_entity.get("category")
                )
            )
            self.address_repository.update(
                _id=self.data_address.get("id"),
                street=self.data_address.get('street'),
                number=self.data_address.get('number'),
                complement=self.data_address.get('complement'),
                neighborhood=self.data_address.get('neighborhood'),
                zip_code=self.data_address.get('zip_code'),
                city=self.data_address.get('city'),
                state=self.data_address.get('state'),
                country=self.data_address.get('country'),
                entity=instance_entity,
            )
            self.contact_repository.update(
                email=self.data_contact["email"],
                phone_number=self.data_contact["phone_number"],
                entity=instance_entity,
            )
        except Exception as error:
            raise Exception(f'Erro on update Organization {error}')
        else:
            return {
                'message': 'Entidade atualizada com sucesso!',
            }

    def delete(self, id: int = None):
        try:
            self.repository.delete(_id=id)
        except Exception as error:
            raise Exception(f'Erro on update Organization {error}')
        else:
            return "Item deletado!"
