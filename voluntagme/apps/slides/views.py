from django.shortcuts import render

from django.views import generic

from .models import Slide


class IndexView(generic.ListView):
    template_name = 'pages/home.html'
    context_object_name = 'slides_list'

    def get_queryset(self):
        """Return the last 3 published slides."""
        return Slide.objects.order_by('-published_at')[:3]