# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0051_auto_20170609_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominationinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default=None, max_length=20, null=True),
        ),
    ]