# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = patterns('',
	#  causes:discover
	url(_(r'^discover/$'), views.CausesListView.as_view(), name='discover'),
   	# causes:view_cause
   	url(r'^discover/(?P<category>[\w\-]+)/$',
   		views.CausesListView.as_view(),
        name='category_list'),
   	# causes:view_cause
   	url(r'^discover/(?P<category>[\w\-]+)/(?P<slug>[\w\-]+)/$',
   		views.CauseDetailView.as_view(),
        name='detail_cause'),
   	# causes:post_cause_step2
   	url(r'^details/(?P<slug>[\w\-]+)/$', views.CauseUpdateView.as_view(),
        name='post_cause_step2'),

)
