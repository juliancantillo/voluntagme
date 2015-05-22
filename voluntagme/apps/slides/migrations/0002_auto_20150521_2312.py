# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='call_to_action',
            field=models.CharField(default=b'View more', max_length=50),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(max_length=140),
        ),
    ]
