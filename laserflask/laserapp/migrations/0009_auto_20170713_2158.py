# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 18:58
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('laserapp', '0008_auto_20170713_2149'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='laserapp',
            managers=[
                ('all_products', django.db.models.manager.Manager()),
            ],
        ),
    ]