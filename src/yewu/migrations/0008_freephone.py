# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-07 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yewu', '0007_auto_20180926_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreePhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30, verbose_name='手机号')),
                ('createtime', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
    ]