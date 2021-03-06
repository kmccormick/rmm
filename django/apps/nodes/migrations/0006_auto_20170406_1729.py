# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('nodes', '0005_remove_node_fqdn'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodes.Node')),
            ],
        ),
        migrations.CreateModel(
            name='NodeSitePurpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='nodesite',
            name='purpose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodes.NodeSitePurpose'),
        ),
        migrations.AddField(
            model_name='nodesite',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='node',
            name='sites',
            field=models.ManyToManyField(through='nodes.NodeSite', to='sites.Site'),
        ),
    ]
