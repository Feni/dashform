# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-18 03:50
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='DashField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('datatype', models.CharField(choices=[(b'BOOL', b'Boolean'), (b'NUM', b'Number'), (b'TXT', b'Text')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DashTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='dashfield',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashformapp.DashTable'),
        ),
        migrations.AddField(
            model_name='dashentry',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashformapp.DashTable'),
        ),
    ]
