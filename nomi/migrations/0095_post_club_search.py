# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0094_auto_20170624_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='club_search',
            field=models.ManyToManyField(blank=True, related_name='post_club', to='nomi.Post'),
        ),
    ]
