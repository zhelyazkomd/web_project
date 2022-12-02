from web_project.events.models import Event


def get_event_by_slug(slug_event):
    return Event.objects \
        .filter(slug=slug_event).get()
