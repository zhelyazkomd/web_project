from django.contrib.auth.decorators import login_required
from django.urls import path, include

from web_project.techreview.views import CreateFeaturedView, AllFeaturedView

urlpatterns = (
    path('create/', login_required(CreateFeaturedView.as_view()), name='create featured'),
    path('', include([
        path('all/',AllFeaturedView.as_view(), name='all featured'),
        # path('create/',),
    ])),
)
