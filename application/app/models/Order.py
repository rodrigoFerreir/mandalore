from . import *


class Order(BaseClassModel):

    date_order = models.DateTimeField(auto_now_add=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="orders")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="address_destination")
    
    def __str__(self):
        return f'{self.entity.name} - {self.date_order}'
