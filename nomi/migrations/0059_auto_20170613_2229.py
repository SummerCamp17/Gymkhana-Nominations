# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0058_auto_20170613_0810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nomination',
            options={'ordering': ('opening_date',)},
        ),
    ]