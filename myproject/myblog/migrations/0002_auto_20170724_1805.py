# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='名称'),
        ),
    ]
