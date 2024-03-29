from . import *


class ProductCategory(BaseClassModel):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'product_categories'
        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategories'

    def __str__(self):
        return self.name
