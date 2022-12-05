from enum import Enum
from cloudinary import models as cloudinary_models
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from web_project.core.model_mixin import ChoicesEnumMixin

UserModel = get_user_model()


class Featured(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_CATEGORY_LENGTH = 30
    MAX_SUMMARY_LENGTH = 50
    MAX_TEXT_ARTICLE_LENGTH = 1500

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

    article_text = models.TextField(
        max_length=MAX_TEXT_ARTICLE_LENGTH,
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
    )

    photo = cloudinary_models.CloudinaryField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.title}')
        return super().save(*args, **kwargs)
