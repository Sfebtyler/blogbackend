# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogdata', '0006_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='http://127.0.0.1:8000/posts/images/')),
                ('postid', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterField(
            model_name='post',
            name='posttext',
            field=models.CharField(blank=True, default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='post',
            name='postimage',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blogdata.Image'),
        ),
    ]
