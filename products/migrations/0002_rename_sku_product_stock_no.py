# Generated by Django 3.2 on 2022-05-13 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sku',
            new_name='stock_no',
        ),
    ]
