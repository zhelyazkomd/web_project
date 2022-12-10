from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from web_project.common.models import RegisterEvent
from web_project.common.uitls import get_current_url_path
from web_project.core.other_validators import register_user_in_event, create_user_register_in_event
from web_project.events.forms import CreateEventForm, EditEventForm
from web_project.events.models import Event
from web_project.events.utils import get_event_by_slug, remaining_event_capacity


class CreateEventView(views.CreateView):
    template_name = 'event/create-event.html'
    form_class = CreateEventForm

    # TODO: CHANGE TO EVENT DETAILS
    # success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        return render(request, 'event/create-event.html', {'form': form})


class AllEventView(views.ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event/all-events.html'
    # template_name = 'event/test.html'


class EditEventView(views.UpdateView):
    model = Event
    template_name = 'event/edit-event.html'
    form_class = EditEventForm
    slug_url_kwarg = 'slug'

    success_url = reverse_lazy('show all events')


class DeleteEventView(views.DeleteView):
    model = Event
    template_name = 'event/delete-event.html'
    success_url = reverse_lazy('show all events')


class DetailsEventView(views.DetailView):
    model = Event
    template_name = 'event/details-event.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        current_slug = self.kwargs.get(self.slug_url_kwarg)
        current_event = get_event_by_slug(current_slug).pk
        event_capacity = get_event_by_slug(current_slug).capacity
        register_user = RegisterEvent.objects.filter(event_id=current_event).count()
        data = super().get_context_data(**kwargs)

        data['free_slots'] = remaining_event_capacity(event_capacity, register_user)

        return data

    '''Delete in final version'''
    # pk_url_kwarg = 'event_name'

    # def get_context_data(self, **kwargs):
    #     pass
    # def get_slug_field(self):
    #
    #
    #
    # def get_queryset(self):
    #     # get_slug = Event.objects.filter(pk=request.pk)
    #     # return super().get_queryset().filter(event__name=self.kwargs['event_name'])
    #     # return get_object_or_404(Event, slug=self.kwargs['event_slug'])
    #     self.event_slug = get_object_or_404(Event, slug=self.kwargs['slug'])
    #     print(self.event_slug)
    #     return Event.objects.filter(slug='12-big-data2')


def register_event(request, event_id):
    registered = register_user_in_event(request, event_id)

    if registered:
        registered.delete()
    else:
        create_user_register_in_event(request, event_id)

    return redirect(get_current_url_path(request))
