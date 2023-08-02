
from models import Organization, Address


class ServiceOrganization():

    def create(self, data_request: dict):
        data_organization = data_request['org']
        data_address = data_request['org']['address']

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
        except Exception as error:
            raise Exception(f'Error on create Organization {error}')
        else:
            return {
                'message': 'Organização criada com sucesso!',
                'data': {
                    'name': organization.name,
                }
            }
