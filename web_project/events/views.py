from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from web_project.events.forms import CreateEventForm, EditEventForm


class CreateEventView(views.CreateView):
    template_name = 'event/create-event.html'
    form_class = CreateEventForm

    #TODO: CHANGE TO EVENT DETAILS
    # success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        return render(request, 'event/create-event.html', {'form': form})


class EditEventView(views.UpdateView):
    template_name = 'event/edit-event.html'
    form_class = EditEventForm
