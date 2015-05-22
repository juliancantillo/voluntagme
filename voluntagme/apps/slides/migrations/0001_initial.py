# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('link', models.URLField(default=b'#')),
                ('call_to_action', models.TextField(default=b'View more')),
                ('image', models.ImageField(max_length=500, null=True, upload_to=b'slides', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
