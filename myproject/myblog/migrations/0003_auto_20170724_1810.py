# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20170724_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='myblog.Tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='life', max_length=20, verbose_name='名称'),
            preserve_default=False,
        ),
    ]
