
from django.urls import path, include

from web_project.accounts.views import SignUpView, SignInView, SignOutView, UserEditView, UserDeleteView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile/<int:pk>/', include([
        path('edit/', UserEditView.as_view(), name='edit profile'),
        path('delete/', UserDeleteView.as_view(), name='delete profile'),
    ])),
)