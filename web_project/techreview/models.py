from enum import Enum
from cloudinary import models as cloudinary_models
from django.db import models

from web_project.core.model_mixin import ChoicesEnumMixin


class TypeOfEvent(ChoicesEnumMixin, Enum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5


class Featured(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_CATEGORY_LENGTH = 30
    MAX_SUMMARY_LENGTH = 50
    MAX_DESCRIPTION_LENGTH = 255

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        blank=False,
        null=False,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        blank=False,
        null=False,
    )

    summary = models.TextField(
        max_length=MAX_SUMMARY_LENGTH,
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        blank=False,
        null=False,
    )

    photo = cloudinary_models.CloudinaryField(
        null=True,
        blank=True,
    )
