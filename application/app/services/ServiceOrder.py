from itertools import product
from . import *

class ServiceOrder(BaseService):

    def __init__(self, data:dict) -> None:
        self.data_order = data
        self.data_order_address = data.get("address")
        self.data_item_order = data.get("itens")
        self.repository = OrderRepository()
        self.repository_item_order = ItemOrderRepository()
        self.repository_entity = EntityRepository()
        self.repository_address = AddressRepository()
        self.repository_product = ProductRepository()
    
    def create(self):

        try:
            entity = None
            address = None
            
            if self.data_order.get("cpf_cnpj"):
                entity = self.repository_entity.get_by_cpf_cnpj(cpf_cnpj=self.data_order.get("cpf_cnpj"))
            
            if self.data_order_address:
                address = self.repository_address.get_or_create(
                    street=self.data_order_address.get('street'),
                    number=self.data_order_address.get('number'),
                    complement=self.data_order_address.get('complement'),
                    neighborhood=self.data_order_address.get('neighborhood'),
                    zip_code=self.data_order_address.get('zip_code'),
                    city=self.data_order_address.get('city'),
                    state=self.data_order_address.get('state'),
                    country=self.data_order_address.get('country'),
                    entity=entity
                )
            order = self.repository.create(
                entity= entity,
                address= address
            )
            if self.data_item_order:
                self.data_order['order_id'] = order.id
                self.add_item()
            
        except Exception as error:
            raise Exception(f'Error on create Order {error}')
        else:
            return {
                "message": "Pedito criado com sucesso!",
                "data": OrderSerializer(order).data
            }

    def get(self):
        try:
            _result = []
            for order in self.repository.get():
                _result.append(OrderSerializer(order).data)

        except Exception as error:
            raise Exception(f'Erro on get Orders {error}')
        else:
            return _result

    def update(self):
        try:
            entity = None
            address = None
            if self.data_order.get("cpf_cnpj"):
                entity = self.repository_entity.get_by_cpf_cnpj(cpf_cnpj=self.data_order.get("cpf_cnpj"))
            
            if self.data_order_address:
                address = self.repository_address.get_or_create(
                    street=self.data_order_address.get('street'),
                    number=self.data_order_address.get('number'),
                    complement=self.data_order_address.get('complement'),
                    neighborhood=self.data_order_address.get('neighborhood'),
                    zip_code=self.data_order_address.get('zip_code'),
                    city=self.data_order_address.get('city'),
                    state=self.data_order_address.get('state'),
                    country=self.data_order_address.get('country'),
                    entity=entity
                )
            
            self.repository.update(_id=self.data_order["order_id"], entity=entity, address=address)

            order = self.repository.get_by_id(_id=self.data_order["order_id"])
            for item in self.data_item_order:
                if item.get("product_id") not in [i.product.id for i in order.itens_order.all()]:
                    self.add_item()
            order.save()
        except Exception as error:
            raise Exception(f'Erro on update Order {error}')
        else:
            return {
                'message': 'Pedito atualizado com sucesso!',
                'data': OrderSerializer(order).data
            }

    def delete(self):
        try:
           self.repository.delete(_id = self.data_order['order_id'])
        except Exception as error:
            raise Exception(f'Erro on delete Order {error}')
        else:
            return "Item deletado!"
    

    def add_item(self):
        try:
            order = self.repository.get_or_create_by_id(_id=self.data_order['order_id'])
            if order:
                for item_order in self.data_item_order:
                    product = self.repository_product.get_by_id(_id=item_order.get("product_id"))
                    total_value = int(product.price * item_order.get('qtd'))
                    
                    self.repository_item_order.create(
                        product=product,
                        amount=item_order.get('qtd'),
                        order=order,
                        total_value=total_value,
                    )
                order.save()
        except Exception as error:
            raise Exception(f'Erro on add_item Order {error}')
        else:
            return {
                'message': 'Pedito criado com sucesso!',
                "data": OrderSerializer(order).data
            }
