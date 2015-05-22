# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0003_auto_20150521_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='published_at',
            field=models.DateTimeField(default=datetime.date(2015, 5, 21), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
