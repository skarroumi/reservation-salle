# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-24 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20180324_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaire',
            name='HeureFin',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]