# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2020-09-27 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u5217\u540d', max_length=100)),
                ('data_type', models.CharField(blank=True, help_text='\u6570\u636e\u7c7b\u578b', max_length=100, null=True)),
                ('is_null', models.NullBooleanField(choices=[(True, 'NULL'), (False, 'NOT NULL')], help_text='\u53ef\u7a7a')),
                ('default_value', models.CharField(blank=True, help_text='\u9ed8\u8ba4\u503c', max_length=100, null=True)),
                ('comment', models.TextField(blank=True, help_text='\u6ce8\u91ca', max_length=5000, null=True)),
                ('is_comment_dirty', models.BooleanField(default=False)),
                ('is_enum', models.BooleanField(default=False)),
                ('other_enums', models.TextField(blank=True, default='', help_text='\u672a\u5339\u914d\u7684\u679a\u4e3e\u503c', max_length=2000, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u6570\u636e\u5e93\u540d', max_length=100, unique=True)),
                ('config', models.CharField(help_text='\u914d\u7f6e', max_length=100, unique=True)),
                ('engine', models.CharField(blank=True, default='InnoDB', help_text='\u5f15\u64ce', max_length=10, null=True)),
                ('charset', models.CharField(blank=True, default='utf8', help_text='\u7f16\u7801', max_length=100, null=True)),
                ('comment', models.TextField(blank=True, default='TBD', help_text='\u6ce8\u91ca', max_length=5000, null=True)),
                ('enable', models.NullBooleanField(choices=[(True, 'on'), (False, 'off')], default=True, help_text='\u662f\u5426\u542f\u7528')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u7d22\u5f15\u540d', max_length=100)),
                ('type', models.CharField(blank=True, choices=[('KEY', 'KEY'), ('PRIMARY KEY', 'PRIMARY KEY'), ('UNIQUE KEY', 'UNIQUE KEY')], help_text='\u7c7b\u578b', max_length=100, null=True)),
                ('include_columns', models.CharField(blank=True, help_text='\u5305\u542b\u5b57\u6bb5', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u8868\u540d', max_length=100)),
                ('engine', models.CharField(blank=True, help_text='\u5f15\u64ce', max_length=10, null=True)),
                ('charset', models.CharField(blank=True, help_text='\u7f16\u7801', max_length=100, null=True)),
                ('comment', models.TextField(blank=True, help_text='\u6ce8\u91ca', max_length=5000, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Database')),
            ],
        ),
        migrations.AddField(
            model_name='index',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Table'),
        ),
        migrations.AddField(
            model_name='column',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Table'),
        ),
        migrations.AlterUniqueTogether(
            name='table',
            unique_together=set([('database', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='index',
            unique_together=set([('table', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='column',
            unique_together=set([('table', 'name')]),
        ),
    ]
