# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laserapp', '0002_auto_20170711_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laserapp',
            name='desc',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
    ]
