# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Algorithm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlgoServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(default=None)),
                ('port', models.IntegerField(default=0)),
            ],
        ),
    ]