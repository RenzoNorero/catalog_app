# Generated by Django 4.1.7 on 2023-02-26 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_producto_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.CharField(default='59255596', max_length=8),
        ),
    ]
