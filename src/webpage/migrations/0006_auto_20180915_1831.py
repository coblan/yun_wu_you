# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-15 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_auto_20180915_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='优先级'),
        ),
        migrations.AddField(
            model_name='actiongroup',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='优先级'),
        ),
        migrations.AddField(
            model_name='mainmenu',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='优先级'),
        ),
    ]
