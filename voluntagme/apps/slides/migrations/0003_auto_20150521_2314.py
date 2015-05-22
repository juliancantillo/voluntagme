# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_auto_20150521_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='description',
            field=models.CharField(max_length=140, blank=True),
        ),
    ]
