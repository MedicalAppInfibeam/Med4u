# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyHealthApp', '0003_auto_20170622_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bodypart',
            old_name='bodypart',
            new_name='bodypartname',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_pic',
            field=models.ImageField(blank=True, null=True, upload_to='doctors'),
        ),
    ]
