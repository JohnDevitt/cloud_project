# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montagemaker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='montageelementcontainer',
            name='id',
        ),
        migrations.AlterField(
            model_name='montageelementcontainer',
            name='title',
            field=models.CharField(max_length=3000, serialize=False, primary_key=True),
        ),
    ]
