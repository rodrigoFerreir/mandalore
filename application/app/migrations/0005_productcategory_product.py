# Generated by Django 4.2.3 on 2023-08-17 21:50

import core.utils.select_current_values_db
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_entity_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=core.utils.select_current_values_db.get_current_date_time_database)),
                ('updated_at', models.DateTimeField(default=core.utils.select_current_values_db.get_current_date_time_database, null=True)),
                ('username_create', models.CharField(default=core.utils.select_current_values_db.get_current_user_database, max_length=255, null=True)),
                ('username_update', models.CharField(default=core.utils.select_current_values_db.get_current_user_database, max_length=255, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'ProductCategory',
                'verbose_name_plural': 'ProductCategories',
                'db_table': 'product_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=core.utils.select_current_values_db.get_current_date_time_database)),
                ('updated_at', models.DateTimeField(default=core.utils.select_current_values_db.get_current_date_time_database, null=True)),
                ('username_create', models.CharField(default=core.utils.select_current_values_db.get_current_user_database, max_length=255, null=True)),
                ('username_update', models.CharField(default=core.utils.select_current_values_db.get_current_user_database, max_length=255, null=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=6, max_digits=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.productcategory')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
    ]
