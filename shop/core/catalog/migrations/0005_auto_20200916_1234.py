# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-16 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200916_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slug',
            name='slug',
            field=models.CharField(default=None, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]