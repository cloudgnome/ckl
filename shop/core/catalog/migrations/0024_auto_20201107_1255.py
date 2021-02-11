# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-07 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20201104_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.PositiveIntegerField(choices=[(1, 'Игротека'), (2, 'Велис'), (3, 'Тигрес')], default=1, null=True, verbose_name='Склад'),
        ),
    ]