# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-13 12:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_auto_20201107_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='view',
        ),
    ]
