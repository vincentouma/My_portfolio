# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-02 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vin', '0003_auto_20190920_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='skill_pics')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
