# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogdata', '0011_auto_20160909_1814'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
