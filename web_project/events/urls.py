from django.contrib.auth.decorators import login_required
from django.urls import path, include

from web_project.events.views import CreateEventView, EditEventView, AllEventView, DetailsEventView

urlpatterns = (
    path('create/', login_required(CreateEventView.as_view()), name='create event'),
    path('',
         include([
             path('all/', AllEventView.as_view(), name='show all events'),
             # path('edit/<slug:event_slug>/', login_required(EditEventView.as_view()), name='edit event'),
             path('details/<slug>/', login_required(DetailsEventView.as_view()), name='details event'),

         ])),

)
