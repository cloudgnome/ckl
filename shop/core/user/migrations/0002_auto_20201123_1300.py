# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-23 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
    ]
