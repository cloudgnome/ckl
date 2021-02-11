# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-09-16 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_page_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branddescription',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='categorydescription',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='citydescription',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='pagedescription',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.PositiveIntegerField(choices=[(1, 'Игротека'), (2, 'Велис'), (3, 'Тигрес')], default=1, null=True, verbose_name='Склад'),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='tagdescription',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]