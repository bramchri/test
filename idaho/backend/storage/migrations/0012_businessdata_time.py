# Generated by Django 2.1.3 on 2018-11-14 08:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0011_businessdata_is_imported'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdata',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 8, 57, 58, 532447, tzinfo=utc)),
        ),
    ]
