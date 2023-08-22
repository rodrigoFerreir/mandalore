from . import *

class ServiceOrder(BaseService):

    def __init__(self, data:dict) -> None:
        self.data_order = data
        self.data_item_order = data.get("itens")
        self.repository = OrderRepository()
        self.repository_item_order = ItemOrderRepository()
        self.repository_entity = EntityRepository()
        self.repository_address = AddressRepository()
    
    def create(self):

        try:
            entity = self.repository_entity.get_by_cpf_cnpj(cpf_cnpj=self.data_order["cpf_cnpj"])
            #address = self.repository_address.get() # TODO: criar get_or_create
            order = self.repository.create(
                entity= entity,
                address= entity.addresses.last()
            )
        except Exception as error:
            raise Exception(f'Error on create Order {error}')
        else:
            return {
                'message': 'Pedito criado com sucesso!',
                "data": {
                    "date": order.date_order.strftime("%m/%d/%Y - %H:%M:%S"),
                    "entity_data": EntitySerializer(order.entity).data,
                    "address": AddressSerializer(order.entity.addresses.last()).data,
                    "itens":[],
                }
            }

    def get(self):
        try:
           ...
        except Exception as error:
            raise Exception(f'Erro on get Orders {error}')
        else:
            return []

    def update(self):
        try:
            ...
        except Exception as error:
            raise Exception(f'Erro on update Order {error}')
        else:
            return {
                'message': 'Pedito atualizado com sucesso!',
            }

    def delete(self, id: int):
        try:
           ...
        except Exception as error:
            raise Exception(f'Erro on update Order {error}')
        else:
            return "Item deletado!"