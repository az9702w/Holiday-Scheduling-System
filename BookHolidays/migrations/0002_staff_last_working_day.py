# Generated by Django 3.1.4 on 2021-02-10 03:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BookHolidays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='last_working_day',
            field=models.DateField(default=datetime.datetime(2021, 2, 10, 3, 34, 5, 992106, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
