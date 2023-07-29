# Generated by Django 4.2.3 on 2023-07-29 14:55

import core.utils.select_current_values_db
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_alter_organization_options_alter_organization_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='created_at',
            field=models.DateTimeField(default=core.utils.select_current_values_db.get_current_date_time_database),
        ),
        migrations.AddField(
            model_name='organization',
            name='updated_at',
            field=models.DateTimeField(default=core.utils.select_current_values_db.get_current_date_time_database, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='username_create',
            field=models.CharField(default=core.utils.select_current_values_db.get_current_user_database, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='username_update',
            field=models.CharField(default=core.utils.select_current_values_db.get_current_user_database, max_length=255, null=True),
        ),
    ]
