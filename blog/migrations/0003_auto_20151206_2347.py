# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151206_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at', '-pk')},
        ),
        migrations.AddField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 6, 14, 47, 11, 602211, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 6, 14, 47, 15, 370889, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
