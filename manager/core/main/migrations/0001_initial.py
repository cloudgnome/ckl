# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-14 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_auto_20200914_0719'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveIntegerField(choices=[(1, 'Product'), (2, 'Category'), (3, 'Brand'), (4, 'Tag')])),
                ('text', models.CharField(max_length=255)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Percent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(verbose_name='Процентная наценка')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frm', models.PositiveIntegerField()),
                ('to', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('database', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('model', models.CharField(max_length=50, verbose_name='Артикул')),
                ('active', models.BooleanField(default=1, verbose_name='Актив')),
            ],
            options={
                'verbose_name': 'Новые товары',
                'verbose_name_plural': 'Новые товары',
                'ordering': ['-active'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.PositiveIntegerField(choices=[(1, 'Google Merchant'), (2, 'Синхронизация цен'), (3, 'Facebook Merchant')])),
                ('task_status', models.PositiveIntegerField(choices=[(1, 'В обработке'), (2, 'Выполнено')])),
            ],
        ),
        migrations.CreateModel(
            name='Tigres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('model', models.CharField(max_length=50, verbose_name='Артикул')),
                ('active', models.BooleanField(default=1, verbose_name='Актив')),
                ('retail_price', models.PositiveIntegerField()),
                ('big_opt_price', models.PositiveIntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tigres_product', to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Тигрес',
                'verbose_name_plural': 'Тигрес',
                'ordering': ['-active'],
            },
        ),
        migrations.CreateModel(
            name='TigresGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='data/products/%Y/%m/%d', verbose_name='Картинка')),
                ('position', models.PositiveIntegerField(blank=True, default=0, verbose_name='Порядоковый номер')),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='main.Tigres')),
            ],
            options={
                'verbose_name': 'Картины Тигрес',
                'verbose_name_plural': 'Картины Тигрес',
            },
        ),
        migrations.AddField(
            model_name='percent',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Price'),
        ),
    ]
