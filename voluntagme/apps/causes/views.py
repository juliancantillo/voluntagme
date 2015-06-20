# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView, CreateView

from core.forms import FormListView
from core import constants
from .models import Cause
from .forms import CauseCreateForm, CauseUpdateForm

class CausesListView(FormView):
    """docstring for CausesListView"""
    model = Cause
    form_class = CauseCreateForm
    template_name = "causes/list.html"

    def form_valid(self, form):
        cause = form.save()
        print 'success'
        return redirect('causes:post_cause_step2', cause.slug)  	

    def get_context_data(self, **kwargs):
        context = super(CausesListView, self).get_context_data(**kwargs)

        if 'category' in self.kwargs:
        	if self.kwargs['category'] != 'all':
        		context['object_list'] = Cause.objects.filter(category=self.kwargs['category'])	
	    	else:
	    		context['object_list'] = Cause.objects.all()
    	else:
    		context['object_list'] = Cause.objects.all()

        context['categories'] = constants.MENU_CAUSE_CATEGORY

        return context


class CauseUpdateView(UpdateView):
    model = Cause
    slug_field = 'slug'
    template_name = "causes/edit.html"
    form_class = CauseUpdateForm

class CauseDetailView(DetailView):
    model = Cause
    template_name = "causes/detail.html"