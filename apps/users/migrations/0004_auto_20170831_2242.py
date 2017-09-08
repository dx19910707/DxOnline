# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-31 22:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170831_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加的时间'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=110, verbose_name='顺序'),
        ),
    ]