# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-12 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_remove_order_specialcargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='specialCargo',
            field=models.BooleanField(choices=[(0, 'Нет'), (1, 'Да')], default=1),
        ),
    ]
