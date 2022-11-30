from django.contrib.auth.decorators import login_required
from django.urls import path, include

from web_project.events.views import CreateEventView

urlpatterns = (
    path('create/', login_required(CreateEventView.as_view()), name='create event'),
)