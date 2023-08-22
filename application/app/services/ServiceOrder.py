from . import *

class ServiceOrder(BaseService):
    def create(self):

        try:
           ...
        except Exception as error:
            raise Exception(f'Error on create Order {error}')
        else:
            return {
                'message': 'Pedito criado com sucesso!',
                "data": []
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