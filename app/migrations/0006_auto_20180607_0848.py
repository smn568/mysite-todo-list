# Generated by Django 2.0.6 on 2018-06-07 00:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180603_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertodo',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 7, 8, 48, 20, 434546), verbose_name='截至时间'),
        ),
    ]
