from django.contrib.auth.decorators import login_required
from django.urls import path, include

from web_project.techreview.views import CreateFeaturedView, AllFeaturedView, EditFeaturedView, DeleteFeaturedView, \
    DetailsFeaturedView

urlpatterns = (
    path('create/', login_required(CreateFeaturedView.as_view()), name='create featured'),
    path('', include([
        path('all/', AllFeaturedView.as_view(), name='all featured'),
        path('edit/<slug>/', EditFeaturedView.as_view(), name='edit featured'),
        path('details/<slug>/', DetailsFeaturedView.as_view(), name='details featured'),
        path('delete/<slug>/', DeleteFeaturedView.as_view(), name='delete featured'),
        # path('create/',),
    ])),
)
