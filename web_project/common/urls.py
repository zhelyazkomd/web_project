from django.urls import path

from web_project.common.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)