# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_auto_20170330_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='ipaddrs',
        ),
        migrations.RemoveField(
            model_name='node',
            name='macs',
        ),
        migrations.AddField(
            model_name='node',
            name='hwtype',
            field=models.CharField(blank=True, choices=[('hw', 'Physical'), ('vm', 'Virtual'), ('ss', 'SaaS')], default='hw', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='os',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='ostype',
            field=models.CharField(blank=True, choices=[('win', 'Windows'), ('lnx', 'Linux'), ('unx', 'Unix'), ('mac', 'Mac OS X / MacOS'), ('mob', 'Mobile Device OS'), ('emb', 'Embedded Device OS - switches, routers, etc.'), ('oth', 'Other OS Type')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='nodeip',
            name='node',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='nodes.Node'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nodemac',
            name='node',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='nodes.Node'),
            preserve_default=False,
        ),
    ]
