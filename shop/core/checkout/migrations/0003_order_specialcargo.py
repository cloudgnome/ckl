# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-11 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200929_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='SpecialCargo',
            field=models.BooleanField(default=0, verbose_name='Спецгруз?'),
        ),
    ]
