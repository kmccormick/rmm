# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0006_auto_20170406_1729'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nodesite',
            unique_together=set([('node', 'purpose')]),
        ),
    ]
