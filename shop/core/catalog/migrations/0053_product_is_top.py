# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-25 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0052_auto_20201224_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_top',
            field=models.BooleanField(default=0),
        ),
    ]
