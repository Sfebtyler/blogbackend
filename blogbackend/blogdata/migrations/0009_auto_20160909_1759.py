# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogdata', '0008_auto_20160909_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='http://127.0.0.1:8000/posts/images/'),
        ),
    ]
