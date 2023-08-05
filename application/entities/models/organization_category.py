from django.db import models
from core.utils.base import BaseClassModel


class OrganizationCategory(BaseClassModel):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'organization_categories'
        verbose_name = 'OrganizationCategory'
        verbose_name_plural = 'OrganizationCategories'

    def __str__(self):
        return self.name
