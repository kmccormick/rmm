# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 23:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0004_auto_20170405_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='fqdn',
        ),
    ]