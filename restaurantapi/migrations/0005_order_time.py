# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapi', '0004_auto_20170724_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
