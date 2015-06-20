# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('causes', '0002_auto_20150608_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='image',
            field=models.ImageField(default=b'default/voluntagme-volunteer-causes-need-your-help.jpg', max_length=1000, upload_to=b'causes', blank=True),
        ),
        migrations.AlterField(
            model_name='cause',
            name='volunteers_goal',
            field=models.PositiveIntegerField(default=0, verbose_name='Volunteers Goal', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='cause',
            name='volunteers_qty',
            field=models.PositiveIntegerField(default=0, verbose_name='Volunteers Quantity', validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
