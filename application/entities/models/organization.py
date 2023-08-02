from django.db import models
from core.utils.base import BaseClassModel


class Organization(BaseClassModel):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=22, unique=True)
    _type = models.CharField(max_length=120)

    class Meta:
        db_table = 'organizations'
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return self.name
