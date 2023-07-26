from typing import Any
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'organizations'
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name
