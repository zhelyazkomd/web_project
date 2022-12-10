from web_project.techreview.models import Featured


def get_featured_id_from_slug(current_slug):
    return Featured.objects.filter(slug=current_slug).get()