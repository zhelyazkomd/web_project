from django.contrib import admin

from web_project.techreview.models import Featured


@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    pass