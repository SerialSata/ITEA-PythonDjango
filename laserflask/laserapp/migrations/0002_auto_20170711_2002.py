# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laserapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laserapp',
            options={'verbose_name': 'Laser cutting software', 'verbose_name_plural': 'Laser cutting softwares'},
        ),
        migrations.AlterField(
            model_name='laserapp',
            name='desc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='laserapp',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='laserapp',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]
