from django.contrib import admin

from causes.models import Cause
from django.contrib import admin

# Register your models here.

class CausesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [(
                'title',
                'category',
                'slug',
                'volunteers_goal',
                'volunteers_qty',
                'image',
            )]
        })
    ]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title','description']
    search_fields = ['title','category']

admin.site.register(Cause, CausesAdmin)