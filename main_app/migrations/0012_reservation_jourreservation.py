# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-26 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20180326_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='jourReservation',
            field=models.CharField(choices=[('lundi', 'Lundi'), ('mardi', 'Mardi'), ('mercredi', 'Mercredi'), ('jeud', 'Jeudi'), ('vendredi', 'Vendredi'), ('samedi', 'Samedi')], default='Lundi', max_length=15),
        ),
    ]
