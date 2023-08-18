from app.serializers import *
from . import *


class ServiceProduct(BaseService):

    def __init__(self, data: dict = None) -> None:
        self.data_product = data
        self.repository = ProductRepository()
        self.category_repository = ProductCategoryRepository()

    def create(self):

        try:
            try:
                category = self.category_repository.get_by_name(
                    self.data_product["category"]
                )
            except:
                category = self.category_repository.create(
                    self.data_product["category"]
                )

            instance_product = self.repository.create(
                name=self.data_product['name'],
                price=self.data_product['price'],
                category=category
            )
        except Exception as error:
            raise Exception(f'Error on create Organization {error}')
        else:
            return {
                'message': 'Entidade criada com sucesso!',
                "data": ProductSerializer(instance_product).data,
            }

    def get(self):
        try:
            _result = []
            for item in self.repository.get():
                _result.append(ProductSerializer(item).data)
        except Exception as error:
            raise Exception(f'Erro on get Entities {error}')
        else:
            return _result

    def update(self):
        try:
            ...
        except Exception as error:
            raise Exception(f'Erro on update Organization {error}')
        else:
            return {
                'message': 'Entidade atualizada com sucesso!',
            }

    def delete(self, id: int = None):
        try:
            ...
        except Exception as error:
            raise Exception(f'Erro on update Organization {error}')
        else:
            return "Item deletado!"