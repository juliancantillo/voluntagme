from slides.models import Slide
from django.contrib import admin

# Register your models here.

class SlidesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [(
                'title',
                'description',
                'link',
                'call_to_action',
                'image',
                'published_at',
            )]
        })
    ]
    list_display = ['title','description','published_at']
    search_fields = ['title','published_at']

admin.site.register(Slide, SlidesAdmin)