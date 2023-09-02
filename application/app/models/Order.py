from . import *


class Order(BaseClassModel):

    date_order = models.DateTimeField(auto_now_add=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="address_destination", null=True, blank=True)
    status = models.IntegerField(choices=StatusOrder.choices(), default=StatusOrder.OPEN)
    status_payment = models.IntegerField(choices=StatusPayment.choices(), default=StatusPayment.PENDING)
    total_value_order = models.DecimalField(max_digits=8, decimal_places=6, default=0.0)


    def __str__(self):
        return f'{self.entity.name} - {self.date_order}'

    @property
    def get_status_order(self):
        return StatusOrder(self.status).name.title()
    

    @property
    def get_status_payment(self):
        return StatusPayment(self.status_payment).name.title()


    def _calculate_total_value_order(self):
        for i in self.itens_order.all():
            self.total_value_order += i.total_value
