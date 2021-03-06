# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-13 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_ua', models.CharField(max_length=255, null=True)),
                ('address_ru', models.CharField(max_length=255)),
                ('type', models.PositiveIntegerField(choices=[(1, 'np'), (2, 'd')], default=1)),
            ],
            options={
                'ordering': ['address_ru'],
            },
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_ua', models.CharField(max_length=255, null=True)),
                ('address_ru', models.CharField(max_length=255)),
                ('number', models.PositiveIntegerField(null=True)),
                ('type', models.PositiveIntegerField(choices=[(1, 'np'), (2, 'd')], default=1)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departaments', to='checkout.City')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True, verbose_name='Имя')),
                ('lname', models.CharField(max_length=255, null=True, verbose_name='Фамилия')),
                ('sname', models.CharField(max_length=255, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=16, null=True, verbose_name='Телефон')),
                ('delivery_type', models.PositiveIntegerField(choices=[(1, 'Новая почта'), (2, 'Деливери'), (3, 'УкрПочта'), (4, 'Самовывоз'), (5, 'Курьерская Доставка')], default=4, verbose_name='Способ доставки')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Адрес')),
                ('payment_type', models.PositiveIntegerField(choices=[(1, 'Наличными при получении'), (2, 'Приват 24')], default=1, verbose_name='Способ оплаты')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Новый'), (2, 'Оплачен'), (11, 'Liqpay Оплачен'), (3, 'Отменен'), (10, 'Ждем товар'), (9, 'Опл. ждем'), (7, 'На отправку'), (8, 'Отправлен'), (4, 'Нет связи'), (5, 'Liqpay'), (6, 'Закрыт')], default=1, verbose_name='Статус заказа')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('ttn_created_date', models.DateTimeField(null=True, verbose_name='Дата отправки')),
                ('comment', models.CharField(max_length=1000, null=True, verbose_name='Комментарий к заказу')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='TTH URL')),
                ('ttn', models.CharField(blank=True, max_length=255, null=True, verbose_name='TTH Number')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart', verbose_name='Корзина')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.City', verbose_name='Город')),
                ('departament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.Departament', verbose_name='Отделение')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказ',
                'ordering': ['-created_at'],
            },
        ),
    ]
