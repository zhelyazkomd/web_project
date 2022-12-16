from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from web_project.common.models import FeaturedLike, FeaturedComment
from web_project.techreview.models import Featured


@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ['id', 'title', 'category', 'summary', 'count_of_like', 'count_of_comments',]
    list_filter = ('title', 'category',)
    search_fields = ('id', 'title', 'category')

    @staticmethod
    def count_of_like(obj):
        likes = FeaturedLike.objects.filter(featured_id=obj).count()
        return likes

    @staticmethod
    def count_of_comments(obj):
        comments = FeaturedComment.objects.filter(featured_id=obj).count()
        return comments
