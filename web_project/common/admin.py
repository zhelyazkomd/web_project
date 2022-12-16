from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from web_project.common.models import FeaturedComment
from web_project.techreview.models import Featured


@admin.register(FeaturedComment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ('publication_date_and_time',)
    list_display = ['publication_date_and_time', 'user', 'featured', 'text', 'view_featured_link',]
    list_filter = ('publication_date_and_time',)
    search_fields = ("user", 'featured',)

    #TODO:fix to correct page
    @staticmethod
    def view_featured_link(obj):
        featured_name = Featured.objects.filter(featuredcomment=obj).get().title
        featured = Featured.objects.filter(featuredcomment=obj).get()
        current_featured = featured.id
        url = (
                reverse('admin:techreview_featured_changelist')
                + "?"
                + urlencode({"featured__id":f"{current_featured}"})

        )
        print(url)
        return format_html('<a href="{}">{} Featured</a>', url, current_featured)
