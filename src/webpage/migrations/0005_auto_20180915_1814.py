# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-15 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_action_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actiongroup',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='yewu.Yewu', verbose_name='访问业务'),
        ),
    ]
