# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-07-26 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("form_manager", "0002_auto_20190720_2126"),
        ("api", "0003_auto_20190720_2125"),
    ]

    operations = [
        migrations.AddField(
            model_name="formdata",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="form_manager.UserProfile",
            ),
        )
    ]