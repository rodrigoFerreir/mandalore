# Generated by Django 4.2.3 on 2023-08-30 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_order_address_alter_order_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_order', to='app.order'),
        ),
    ]
