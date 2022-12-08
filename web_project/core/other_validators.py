from web_project.common.models import FeaturedLike


def user_liked_featured(request, featured_id):
    user = request.user.pk
    return FeaturedLike.objects.filter(featured_id=featured_id, user_id=user)


def create_user_like_featured(request, featured_id):
    user = request.user.pk
    return FeaturedLike.objects.create(featured_id=featured_id, user_id=user)
