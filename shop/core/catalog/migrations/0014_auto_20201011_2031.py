# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-11 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20201011_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='retail_price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
    ]
