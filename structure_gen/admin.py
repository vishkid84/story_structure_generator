from django.contrib import admin
from .models import Story

# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'overview',
        'structure_one',
        'example_one',
        'image_url',
    )

    ordering = ('name',)

admin.site.register(Story, StoryAdmin)
