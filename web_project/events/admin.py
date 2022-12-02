from django.contrib import admin

from web_project.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass