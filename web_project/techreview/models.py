from enum import Enum

from django.db import models

from web_project.core.model_mixin import ChoicesEnumMixin


class TypeOfEvent(ChoicesEnumMixin, Enum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5


class Review(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_CATEGORY_LENGTH = 30
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

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        blank=False,
        null=False,
    )

    # rating =

