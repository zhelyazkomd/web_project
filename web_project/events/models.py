from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from cloudinary import models as cloudinary_models
from django.utils.text import slugify

from web_project.core.model_mixin import ChoicesEnumMixin

UserModel = get_user_model()


class TypeOfEvent(ChoicesEnumMixin, Enum):
    online = 'Online'
    presence = 'Presence'


class Event(models.Model):
    MAX_EVENT_NAME_LENGTH = 20
    MAX_COUNTRY_NAME_LENGTH = 56
    MAX_CITY_NAME_LENGTH = 85
    MAX_DESCRIPTION_LENGTH = 150

    event_name = models.CharField(
        max_length=MAX_EVENT_NAME_LENGTH,
        blank=False,
        null=False,
    )
    event_date = models.DateTimeField(
        blank=False,
        null=False,
    )

    type_of_event = models.CharField(
        choices=TypeOfEvent.choices(),
        max_length=TypeOfEvent.max_len(),
        blank=False,
        null=False,

    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        blank=False,
        null=False,
    )

    capacity = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
    )

    starting_time = models.TimeField(
        blank=True,
        null=True,
    )

    country = models.CharField(
        max_length=MAX_COUNTRY_NAME_LENGTH,
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=MAX_CITY_NAME_LENGTH,
        blank=True,
        null=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
    photo = cloudinary_models.CloudinaryField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.event_name}')
        return super().save(*args, **kwargs)
