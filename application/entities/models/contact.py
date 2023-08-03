
from django.db import models
from core.utils.base import BaseClassModel
from .organization import Organization


class Contact(BaseClassModel):
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.email
