# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapi', '0003_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='MenuItem',
        ),
    ]
