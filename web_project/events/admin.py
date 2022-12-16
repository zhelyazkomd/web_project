from django.contrib import admin

from web_project.common.models import RegisterEvent
from web_project.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ['id', 'event_name', 'type_of_event', 'capacity', 'country', 'city', 'registered_user_for_event']
    list_filter = ('type_of_event', 'capacity', 'country', 'city')
    search_fields = ("event_name", 'type_of_event', 'capacity', 'country', 'city')

    @staticmethod
    def registered_user_for_event(obj):
        registered = RegisterEvent.objects.filter(event_id=obj).count()
        return registered

