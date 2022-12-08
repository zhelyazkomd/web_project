from django.urls import path

from web_project.common.views import IndexView, comment_featured, like_featured

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('comment/<int:featured_id>/', comment_featured, name='comment featured'),
    path('like/<int:featured_id>/', like_featured, name='like featured'),
)