# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laserapp', '0004_auto_20170711_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='IBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=30)),
                ('ram', models.PositiveIntegerField()),
                ('cpu', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='laserapp',
            name='desc',
            field=models.TextField(blank=True, help_text='Short description', null=True, verbose_name='Description'),
        ),
    ]
