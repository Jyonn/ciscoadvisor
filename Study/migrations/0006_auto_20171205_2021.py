# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0005_auto_20171205_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='metric',
            field=models.TextField(),
        ),
    ]