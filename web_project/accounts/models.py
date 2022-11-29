from enum import Enum

from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone

from web_project.accounts.managers import AppUserManager
from web_project.core.model_mixin import ChoicesEnumMixin

from cloudinary import models as cloudinary_models


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    Donoshow = 'Do no show'


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        default=timezone.now,
    )

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


# TODO: CREATE VALIDATORS
class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    MAX_INTRODUCTION_LENGTH = 80

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
    )

    age = models.PositiveIntegerField()

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len()
    )

    short_introduction = models.TextField(
        null=True,
        blank=True,
        max_length=MAX_INTRODUCTION_LENGTH,
    )

    photo = cloudinary_models.CloudinaryField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
