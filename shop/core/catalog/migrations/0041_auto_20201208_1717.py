# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-08 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0040_auto_20201129_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.PositiveIntegerField(choices=[(1, 'CKL'), (2, 'Уточняйте цену')], default=1, null=True, verbose_name='Склад'),
        ),
    ]
