# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-24 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20180324_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaire',
            name='HeureDebut',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]