# Generated by Django 4.2.5 on 2023-12-17 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 17, 11, 41, 6, 985659, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 17, 11, 41, 6, 987086, tzinfo=datetime.timezone.utc)),
        ),
    ]
