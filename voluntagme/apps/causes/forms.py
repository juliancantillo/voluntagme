# -*- coding: utf-8 -*-
import os
import logging

from django import forms
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)


from django import forms
from core import constants

class CauseCreateForm(forms.Form):
    title = forms.CharField(max_length=250,
                              label=_('Title'),
                              widget=forms.TextInput(attrs={'placeholder': _('What is the title of the cause?')})
    )

    category = forms.ChoiceField(choices = constants.CHOICES_CAUSE_CATEGORY,
                              required = True,
                              label = _('Category')
    )

    def __init__(self, instance=None, *args, **kwargs):
        super(CauseCreateForm, self).__init__(*args, **kwargs)
        self.instance = instance

    def save(self):
        title = self.cleaned_data.get('title')
        category = self.cleaned_data.get('category')

        if self.instance is None:
            instance = Cause.objects.create(
                title=title, category=category,
            )

        else:
            instance = self.instance
            
            instance.save()

        return instance