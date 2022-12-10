from django.contrib.auth.decorators import login_required
from django.urls import path, include

from web_project.events.views import CreateEventView, EditEventView, AllEventView, DetailsEventView, DeleteEventView, \
    register_event

urlpatterns = (
    path('create/', login_required(CreateEventView.as_view()), name='create event'),
    path('',
         include([
             path('all/', AllEventView.as_view(), name='show all events'),
             path('details/<slug>/', login_required(DetailsEventView.as_view()), name='details event'),
             path('edit/<slug>/', login_required(EditEventView.as_view()), name='edit event'),
             path('delete/<slug>/', login_required(DeleteEventView.as_view()), name='delete event'),
             path('register/<int:event_id>', register_event, name='register user for event'),

         ])),

)

