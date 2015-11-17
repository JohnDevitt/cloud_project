# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('montagemaker', '0002_auto_20151117_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='montageelementcontainer',
            name='auto_increment_id',
            field=models.AutoField(default=datetime.datetime(2015, 11, 17, 14, 41, 27, 570572, tzinfo=utc), serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='montageelementcontainer',
            name='title',
            field=models.CharField(max_length=3000),
        ),
    ]
