# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApConsultancy', '0003_auto_20180712_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeruser',
            name='job',
        ),
    ]