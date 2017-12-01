# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail', models.TextField()),
                ('metric', models.TextField()),
                ('r_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Study.Study')),
            ],
        ),
    ]