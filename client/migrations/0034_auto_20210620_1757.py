# Generated by Django 3.2.4 on 2021-06-20 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0033_auto_20210620_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 17, 57, 9, 414498)),
        ),
        migrations.AlterField(
            model_name='order',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 17, 57, 9, 415496)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 17, 57, 9, 414498)),
        ),
    ]
