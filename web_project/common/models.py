from django.contrib.auth import get_user_model
from django.db import models
# from django.urls import reverse
# from django.utils import timezone
# from django.utils.text import slugify

from web_project.techreview.models import Featured

UserModel = get_user_model()


# class FeaturedPost(models.Model):
#     MAX_LENGTH_TITLE = 100
#     MAX_LENGTH_SUBTITLE = 200
#
#     title = models.CharField(
#         max_length=MAX_LENGTH_TITLE,
#     )
#     subtitle = models.CharField(
#         max_length=MAX_LENGTH_SUBTITLE,
#         blank=True,
#         null=True
#     )
#     content = models.TextField()
#
#     date_posted = models.DateTimeField(
#         default=timezone.now
#     )
#     author = models.ForeignKey(
#         UserModel,
#         on_delete=models.SET_NULL,
#         null=True)
#
#     # def __str__(self):
#     #     return self.author.email + ', ' + self.title[:40]
#
#     def get_absolute_url(self):
#         return reverse('details featured', kwargs={'pk': self.pk})
#
#     @property
#     def number_of_comments(self):
#         return FeaturedComments.objects.filter(post_connected=self).count()
#
#
# class FeaturedComments(models.Model):
#     post_connected = models.ForeignKey(
#         FeaturedPost,
#         related_name='comments',
#         on_delete=models.CASCADE
#     )
#     author = models.ForeignKey(
#         UserModel,
#         on_delete=models.CASCADE
#     )
#     content = models.TextField()
#
#     date_posted = models.DateTimeField(default=timezone.now())


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.user_id:
            self.user_id = self.user
        if not self.featured_id:
            self.featured_id = self.featured.pk
        return super().save(*args, **kwargs)



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
