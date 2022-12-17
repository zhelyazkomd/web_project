from django.contrib.auth.decorators import login_required
from django.urls import path, include

from web_project.accounts.views import SignUpView, SignInView, SignOutView, UserEditView, UserDeleteView, \
    UserDetailsView, password_change

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', login_required(SignOutView.as_view()), name='sign out'),
    path('<int:pk>/', include([
        path('edit/', login_required(UserEditView.as_view()), name='edit profile'),
        path('delete/', login_required(UserDeleteView.as_view()), name='delete profile'),
        path('details/',login_required(UserDetailsView.as_view()), name='details profile'),
        path('change_password/', password_change, name='user change password'),
    ])),
)
