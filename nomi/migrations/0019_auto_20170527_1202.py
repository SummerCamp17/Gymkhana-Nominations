# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0018_auto_20170527_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='persons',
            new_name='post_holders',
        ),
    ]