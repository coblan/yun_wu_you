# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-16 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yewu', '0004_auto_20180916_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldtype',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='优先级'),
        ),
    ]
