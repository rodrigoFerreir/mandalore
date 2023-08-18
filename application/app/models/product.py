from . import *


class Product(BaseClassModel):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=6)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name="products"
    )

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
