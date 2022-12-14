from django.contrib.auth import views as auth_views, login, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from web_project.accounts.forms import SignUpForm, SetPasswordForm
from web_project.accounts.models import Profile
from web_project.accounts.utils import get_user_profile, get_user_email

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

    # TODO:Check return to user profile
    def get_success_url(self):
        # return reverse_lazy('index', kwargs={
        #     'pk': self.request.user.pk,
        # })

        return reverse_lazy('index')


class UserDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'

    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        request_user_pk = self.kwargs.get(self.pk_url_kwarg)

        data = super().get_context_data(**kwargs)
        data['request_user_age'] = get_user_profile(request_user_pk).age
        data['request_user_full_name'] = get_user_profile(request_user_pk).full_name
        data['request_user_email'] = get_user_email(request_user_pk).email
        data['request_user_descriptions'] = get_user_profile(request_user_pk).short_introduction

        return data


@login_required
def password_change(request, pk):
    user = request.user
    form = SetPasswordForm(user=user, data=request.POST or None)

    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect('index')

    return render(request, 'accounts/profile-change-password.html', {'form': form})


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
