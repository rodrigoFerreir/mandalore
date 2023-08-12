from django.db import models
from ..select_current_values_db import get_current_date_time_database, get_current_user_database


class BaseClassModel(models.Model):
    created_at = models.DateTimeField(default=get_current_date_time_database)
    updated_at = models.DateTimeField(default=get_current_date_time_database, null=True)
    username_create = models.CharField(max_length=255, null=True, default=get_current_user_database)
    username_update = models.CharField(max_length=255, null=True, default=get_current_user_database)

    class Meta:
        abstract = True
