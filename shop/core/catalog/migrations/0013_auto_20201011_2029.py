# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-11 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20200929_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.PositiveIntegerField(choices=[(0, 'UAH'), (1, 'EUR'), (2, 'USD')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.PositiveIntegerField(choices=[(1, 'CKL')], default=1, null=True, verbose_name='Склад'),
        ),
    ]
