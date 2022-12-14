from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators

from django.db import models
from django.utils import timezone

from web_project.accounts.managers import AppUserManager
from web_project.core.model_mixin import ChoicesEnumMixin

from cloudinary import models as cloudinary_models

from web_project.core.parameters_validators import validate_is_letters


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


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MIN_FIRST_NAME_LENGTH = 2

    MAX_LAST_NAME_LENGTH = 30
    MIN_LAST_NAME_LENGTH = 2

    MAX_INTRODUCTION_LENGTH = 80

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
        validators=(
            validators.MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            validate_is_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True,
        validators=(
            validators.MinLengthValidator(MIN_LAST_NAME_LENGTH),
            validate_is_letters,
        )
    )

    age = models.PositiveIntegerField()

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        blank=True,
        null=True,
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

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return f'{self.first_name}'
        elif self.last_name:
            return f'{self.last_name}'