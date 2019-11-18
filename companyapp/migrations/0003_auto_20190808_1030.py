# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-08 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0002_remove_company_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='designation',
            field=models.CharField(choices=[('CEO', 'Ceo'), ('CTO', 'Cto'), ('CFO', 'Cfo'), ('SR AS', 'Sr as'), ('SR TS', 'Sr ts'), ('TL', 'Tl'), ('JR STAFF', 'Jr staff')], max_length=100),
        ),
    ]
