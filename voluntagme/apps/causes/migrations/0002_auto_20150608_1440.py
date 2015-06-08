# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('causes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cause',
            old_name='land',
            new_name='volunteers_goal',
        ),
        migrations.AddField(
            model_name='cause',
            name='volunteers_qty',
            field=models.PositiveIntegerField(default=0, verbose_name='Volunteers goal', validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cause',
            name='category',
            field=models.CharField(default=b'', max_length=60, verbose_name='Category', db_index=True, choices=[(b'', 'My cause is realted to'), (b'health', 'Health'), (b'emergencies', 'Emergencies'), (b'education', 'Education'), (b'rescue', 'Rescue'), (b'community', 'Community'), (b'homeless-and-housing', 'Homeless & Housing'), (b'animals', 'Animals'), (b'crisis-support', 'Crisis support'), (b'environtment', 'Environtment'), (b'sports', 'Sports'), (b'others', 'Others')]),
        ),
        migrations.AlterField(
            model_name='cause',
            name='image',
            field=models.ImageField(default=b'default/voluntagme-volunteer-causes-need-your-help.jpg', max_length=1000, upload_to=b'', blank=True),
        ),
    ]
