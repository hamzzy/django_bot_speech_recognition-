# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-11 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.TextField(default='hello'),
        ),
    ]
