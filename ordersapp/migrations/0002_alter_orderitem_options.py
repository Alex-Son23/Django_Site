# Generated by Django 4.0.4 on 2022-06-01 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'элемент заказа', 'verbose_name_plural': 'элементы заказа'},
        ),
    ]
