# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-13 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0028_auto_20180221_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='ltiexercise',
            name='open_in_iframe',
            field=models.BooleanField(default=False, help_text='Open the exercise in an iframe inside the A+ page instead of a new window.'),
        ),
    ]