# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = patterns('',
   url(_(r'^discover/$'), views.CausesListView.as_view(), name='discover'),
)
