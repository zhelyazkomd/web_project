from cloudinary.forms import CloudinaryFileField
from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth.models import Group

from services.ses import SESService
from web_project.accounts.models import Profile

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'age',)

    # save with data for profile
    def save(self, commit=True):
        user = super().save(commit=commit)
        email = user.email

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
            user=user,
        )
        if commit:
            profile.save()

        user_group = Group.objects.get(name='normal_users')
        user.groups.add(user_group)

        SESService().send_email(email=email)

        return user


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = Profile
        fields = "__all__"
        image = CloudinaryFileField(
            options={
                'tags': "directly_uploaded", })


class SetPasswordForm(auth_forms.PasswordChangeForm):
    class Meta:
        model = UserModel
        fields = ['old_password', 'new_password1', 'new_password2']
