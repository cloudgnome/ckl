# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-09-23 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20200916_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Производители', 'verbose_name_plural': 'Производители'},
        ),
    ]
