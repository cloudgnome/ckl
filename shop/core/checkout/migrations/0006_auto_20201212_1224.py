# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-12 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='specialCargo',
            field=models.BooleanField(choices=[(0, 'Нет'), (1, 'Да')]),
        ),
    ]
