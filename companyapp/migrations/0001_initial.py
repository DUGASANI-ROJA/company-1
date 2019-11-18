# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-07 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=2)),
                ('phno', models.IntegerField(default=10)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('qualification', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='upload/')),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
    ]
