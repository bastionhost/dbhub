# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0010_auto_20180912_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='comment',
            field=models.TextField(blank=True, help_text='\u6ce8\u91ca', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='comment',
            field=models.TextField(blank=True, default='TBD', help_text='\u6ce8\u91ca', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='config',
            field=models.URLField(help_text='\u914d\u7f6e', max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='comment',
            field=models.TextField(blank=True, help_text='\u6ce8\u91ca', max_length=5000, null=True),
        ),
    ]