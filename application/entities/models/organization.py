from django.db import models
from core.utils.base import BaseClassModel
from .organization_category import OrganizationCategory


class Organization(BaseClassModel):
    name = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=22, unique=True)
    category = models.ForeignKey(OrganizationCategory, on_delete=models.PROTECT)

    class Meta:
        db_table = 'organizations'
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return self.name
