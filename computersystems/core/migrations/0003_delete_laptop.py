# Generated by Django 4.2.1 on 2023-05-11 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_laptop_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Laptop',
        ),
    ]
