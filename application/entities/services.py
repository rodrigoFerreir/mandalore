
from .models import Organization, Address, Contact
from django.db.models import Q


class ServiceOrganization():

    def create(self, data_request: dict):
        data_organization = data_request['org']
        data_address = data_request['org']['address']
        data_contact = data_request['org']['contact']

        try:
            organization, created = Organization.objects.get_or_create(
                name=data_organization['name'],
                identity=data_organization['identity'],
                _type=data_organization['type'],
            )
            if created:
                Address.objects.create(
                    street=data_address['street'],
                    number=data_address['number'],
                    complement=data_address['complement'],
                    neighborhood=data_address['neighborhood'],
                    zip_code=data_address['zip_code'],
                    city=data_address['city'],
                    state=data_address['state'],
                    country=data_address['country'],
                    organization=organization
                )
                Contact.objects.create(
                    email=data_contact['email'],
                    phone_number=data_contact['phone_number'],
                    organization=organization
                )

        except Exception as error:
            raise Exception(f'Error on create Organization {error}')
        else:
            return {
                'message': 'Organização criada com sucesso!',
                'data': {
                    'name': organization.name,
                }
            }

    def get(self, id: int = None):
        try:
            _result: list = []
            data_query = Organization.objects.all()
            if id:
                data_query = data_query.filter(Q(id=id))

            for item in data_query:
                item_address = Address.objects.filter(organization=item.id)
                item_contact = Contact.objects.filter(organization=item.id)
                _result.append({
                    "_id": item.id,
                    "name": item.name,
                    "cpf_cnpj": item.identity,
                    "type": item._type,
                    "addresses": [{
                        'id': item.id,
                        'street': item.street,
                        'number': item.number,
                        'complement': item.complement,
                        'neighborhood': item.neighborhood,
                        'zip_code': item.neighborhood,
                        'city': item.city,
                        'state': item.state,
                        'country': item.country,
                        'created_at': item.created_at,
                        'updated_at': item.updated_at,
                        'username_create': item.username_create,
                        'username_update': item.username_update,
                    } for item in item_address],
                    "contacts": [{
                        "id": item.id,
                        "email": item.email,
                        "phone_number": item.phone_number,
                    } for item in item_contact]

                })
        except Exception as error:
            raise Exception(f'Erro on get Organization {error}')
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
