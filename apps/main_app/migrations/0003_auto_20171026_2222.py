# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_trip_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='traveler',
            field=models.ManyToManyField(related_name='travelers', to='login_app.User'),
        ),
    ]
