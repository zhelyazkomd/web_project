from django.contrib import admin

from web_project.common.models import FeaturedComment


@admin.register(FeaturedComment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ('text',)
    list_display = ['publication_date_and_time', 'user', 'featured', 'text',]