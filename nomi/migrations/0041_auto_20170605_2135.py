# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-05 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0040_auto_20170605_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='hall_choice',
            field=models.CharField(choices=[('0', 'All'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hall',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default=1, max_length=10),
        ),
    ]
