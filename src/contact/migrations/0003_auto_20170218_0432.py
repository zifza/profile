# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20170218_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='telp',
            field=models.CharField(default='+62', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
