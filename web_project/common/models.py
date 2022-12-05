from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from web_project.techreview.models import Featured

UserModel = get_user_model()


class FeaturedComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    featured = models.ForeignKey(
        Featured,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class FeaturedLike(models.Model):
    featured = models.ForeignKey(
        Featured,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
