# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-10 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')], max_length=20, verbose_name='验证码类型'),
        ),
    ]
