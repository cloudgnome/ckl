# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-03 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0055_auto_20201228_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.PositiveIntegerField(choices=[(1, 'CKL'), (2, 'Уточняйте цену')], default=1, null=True, verbose_name='Склад'),
        ),
    ]
