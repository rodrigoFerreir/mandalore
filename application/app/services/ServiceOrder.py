from . import *

class ServiceOrder(BaseService):

    def __init__(self, data:dict) -> None:
        self.data_order = data
        self.data_item_order = data.get("itens")
        self.repository = OrderRepository()
        self.repository_item_order = ItemOrderRepository()
        self.repository_entity = EntityRepository()
        self.repository_address = AddressRepository()
        self.repository_product = ProductRepository()
    
    def create(self):

        try:
            total_value_order = 0
            entity = self.repository_entity.get_by_cpf_cnpj(cpf_cnpj=self.data_order["cpf_cnpj"])
            #address = self.repository_address.get() # TODO: criar get_or_create
            order = self.repository.create(
                entity= entity,
                address= entity.addresses.last()
            )
            if self.data_item_order:
                self.data_order['order_id'] = order.id
                self.add_item()
            
            #TODO: alterar para unico metodo
            for i in order.itens_order.all():
                total_value_order += i.total_value
        except Exception as error:
            raise Exception(f'Error on create Order {error}')
        else:
            return {
                "message": "Pedito criado com sucesso!",
                "data": {
                    "date": order.date_order.strftime("%m/%d/%Y - %H:%M:%S"),
                    "total_value_order": total_value_order,
                    "entity_data": EntitySerializer(order.entity).data,
                    "address": AddressSerializer(order.entity.addresses.last()).data,
                    "itens":[{
                        "id":item.id,
                        "products": ProductSerializer(item.product).data,
                        "qtd": item.amount,
                        "total_value": item.total_value
                    }
                    for item in order.itens_order.all()],
                }
            }

    def get(self):
        try:
            _result = []
            for order in self.repository.get():
                
                total_value_order = 0
                for i in order.itens_order.all():
                    total_value_order += i.total_value
                
                _result.append({
                    "date": order.date_order.strftime("%m/%d/%Y - %H:%M:%S"),
                    "total_value_order": total_value_order,
                    "entity_data": EntitySerializer(order.entity).data,
                    "address": AddressSerializer(order.entity.addresses.last()).data,
                    "itens":[{
                        "id":item.id,
                        "products": ProductSerializer(item.product).data,
                        "qtd": item.amount,
                        "total_value": item.total_value
                    }
                    for item in order.itens_order.all()],
                })
        except Exception as error:
            raise Exception(f'Erro on get Orders {error}')
        else:
            return _result

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
    

    def add_item(self):
        try:
            order = self.repository.get_or_create_by_id(_id=self.data_order['order_id'])
            total_value_order = 0
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
            
            for i in order.itens_order.all():
                total_value_order += i.total_value
        except Exception as error:
            raise Exception(f'Erro on add_item Order {error}')
        else:
            return {
                'message': 'Pedito criado com sucesso!',
                "data": {
                    "date": order.date_order.strftime("%m/%d/%Y - %H:%M:%S"),
                    "total_value_order": total_value_order,
                    "entity_data": EntitySerializer(order.entity).data,
                    "address": AddressSerializer(order.entity.addresses.last()).data,
                    "itens":[{
                        "id":item.id,
                        "products": ProductSerializer(item.product).data,
                        "qtd": item.amount,
                        "total_value": item.total_value
                    }
                    for item in order.itens_order.all()],
                }
            }