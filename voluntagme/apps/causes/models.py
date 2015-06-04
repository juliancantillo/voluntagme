# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator

from django.utils import translation

from core.models import TimeStampedModel
from core import constants

@python_2_unicode_compatible
class Cause(TimeStampedModel):
    """A cause is an unique event or a repetitive event where
       volunteers go to develop their labour.
    """
    slug = models.SlugField(max_length=250, db_index=True)
    title = models.CharField(max_length=250, default='',
                             verbose_name=_('Title'))
    description = models.TextField(blank=True, default='',
                                   verbose_name=_('Description'))

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    category = models.CharField(
        db_index=True, blank=False, max_length=60, default='',
        choices=constants.CHOICES_CAUSE_CATEGORY,
        verbose_name=_('Category')
    )

    land = models.PositiveIntegerField(
        default=0, blank=False, verbose_name=_('Volunteers goal'),
        validators=[MinValueValidator(0)]
    )

    image = models.ImageField(
        max_length=1000, blank=True,
        default='default/casa-renta-venta-propiedades-cali.jpg'
    )

    visits = models.PositiveIntegerField(default=0, verbose_name=_('Visits'))

    def __str__(self):
        category = self.category
        title = self.title
        return u' - '.join([category, title])

    class Meta:
        verbose_name = _('Cause')
        verbose_name_plural = _('Causes')
