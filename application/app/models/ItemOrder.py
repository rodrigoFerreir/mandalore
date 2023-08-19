from . import *


class ItemOrder(BaseClassModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="products")
    number = models.IntegerField()
    total_value = models.DecimalField(decimal_places=2)


    def __str__(self) -> str:
        return f'{self.product.name}'