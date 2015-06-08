# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=250)),
                ('title', models.CharField(default=b'', max_length=250, verbose_name='Title')),
                ('description', models.TextField(default=b'', verbose_name='Description', blank=True)),
                ('category', models.CharField(default=b'', max_length=60, verbose_name='Category', db_index=True, choices=[(b'health', 'Health'), (b'emergencies', 'Emergencies'), (b'education', 'Education'), (b'rescue', 'Rescue'), (b'community', 'Community'), (b'homeless-and-housing', 'Homeless & Housing'), (b'animals', 'Animals'), (b'crisis-support', 'Crisis support'), (b'environtment', 'Environtment'), (b'sports', 'Sports'), (b'others', 'Others')])),
                ('land', models.PositiveIntegerField(default=0, verbose_name='Volunteers goal', validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.ImageField(default=b'default/casa-renta-venta-propiedades-cali.jpg', max_length=1000, upload_to=b'', blank=True)),
                ('visits', models.PositiveIntegerField(default=0, verbose_name='Visits')),
                ('created_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Cause',
                'verbose_name_plural': 'Causes',
            },
            bases=(models.Model,),
        ),
    ]
