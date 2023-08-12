from django.db import models
from application.core.utils.base.base import BaseClassModel
from . import Category


class Product(BaseClassModel):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
