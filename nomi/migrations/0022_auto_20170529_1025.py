# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0021_auto_20170527_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nomi.Post'),
        ),
    ]