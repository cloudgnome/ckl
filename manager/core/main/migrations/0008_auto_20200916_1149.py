# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-16 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200916_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta',
            name='model',
            field=models.IntegerField(choices=[(0, 'Product'), (1, 'Category'), (2, 'Brand'), (3, 'Tag'), (4, 'Page'), (5, 'Article'), (6, 'City'), (7, 'Storage')]),
        ),
    ]