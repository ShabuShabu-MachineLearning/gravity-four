# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.IntegerField()),
                ('goban_info', models.TextField()),
            ],
        ),
    ]
