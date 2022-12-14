from django.contrib import admin

from web_project.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ['id', 'event_name', 'type_of_event', 'capacity', 'country', 'city' ]