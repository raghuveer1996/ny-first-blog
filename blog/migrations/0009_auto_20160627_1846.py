# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_results'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='results',
            new_name='result',
        ),
    ]
