# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView, CreateView

from core.forms import FormListView
from .models import Cause
from .forms import CauseCreateForm

class CausesListView(FormListView):
    """docstring for CausesListView"""
    model = Cause
    form_class = CauseCreateForm
    template_name = "causes/list.html"

    def get_context(self):
        context = super(CausesListView, self).get_context_data(**kwargs)