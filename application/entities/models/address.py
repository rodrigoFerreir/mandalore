from django.db import models
from .organization import Organization
from core.utils.base import BaseClassModel


class Address(BaseClassModel):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    complement = models.CharField(max_length=255, null=True, blank=True)
    neighborhood = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'adresses'
        verbose_name = 'Adress'
        verbose_name_plural = 'Adresses'

    def __str__(self):
        return f'{self.number}, {self.street}, {self.neighborhood}, {self.city}'
