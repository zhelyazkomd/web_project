from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from web_project.accounts.forms import SignUpForm
from web_project.accounts.models import Profile

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class SignInView(auth_views.LoginView):
    template_name = "auth/sign-in.html"


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = Profile
    # form_class = UserEditView
    fields = ('first_name', 'last_name', 'gender', 'photo', 'short_introduction',)

    def get_success_url(self):
        # return reverse_lazy('index', kwargs={
        #     'pk': self.request.user.pk,
        # })

        return reverse_lazy('index')


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
