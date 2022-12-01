from django.contrib.auth.decorators import login_required
from django.urls import path, include

from web_project.events.views import CreateEventView, EditEventView

urlpatterns = (
    path('create/', login_required(CreateEventView.as_view()), name='create event'),
    path('edit/<int:pk>', login_required(EditEventView.as_view()), name='edit event'),
)