# Generated by Django 4.2.3 on 2023-08-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='identity',
            field=models.CharField(max_length=22, unique=True),
        ),
    ]