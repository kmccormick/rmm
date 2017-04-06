# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ('full_name',)},
        ),
        migrations.AddField(
            model_name='site',
            name='full_name',
            field=models.CharField(default='foo', editable=False, max_length=400),
            preserve_default=False,
        ),
    ]
