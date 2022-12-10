from web_project.events.models import Event
from web_project.techreview.models import Featured


def get_event_by_slug(slug_event):
    return Event.objects \
        .filter(slug=slug_event).get()


def remaining_event_capacity(capacity, number_of_register_user):
    return capacity - number_of_register_user