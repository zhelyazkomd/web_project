from django.urls import reverse_lazy
from django.views import generic as views

from web_project.events.forms import CreateEventForm


class CreateEventView(views.CreateView):
    template_name = 'event/create-event.html'
    form_class = CreateEventForm

    #TODO: CHANGE TO EVENT DETAILS
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        pass