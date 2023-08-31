from . import *


class ItemOrder(BaseClassModel):

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="products")
    amount = models.IntegerField()
    total_value = models.DecimalField(max_digits=8 , decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="itens_order")


    def __str__(self) -> str:
        return f'{self.product.name} - {self.amount}'
