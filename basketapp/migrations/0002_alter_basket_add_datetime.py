# Generated by Django 4.0.4 on 2022-04-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='add_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='время'),
        ),
    ]
