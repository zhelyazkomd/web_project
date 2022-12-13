from django.contrib.auth import get_user_model

from web_project.accounts.models import Profile

UserModel = get_user_model()


def get_user_profile(user_pk):
    return Profile.objects.filter(user_id=user_pk).get()


def get_user_email(user_pk):
    user = UserModel.objects.filter(id=user_pk).get()
    return user
