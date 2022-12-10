from web_project.common.models import FeaturedLike, RegisterEvent


# TODO: if applicable - merge functions
def user_liked_featured(request, featured_id):
    user = request.user.pk
    return FeaturedLike.objects.filter(featured_id=featured_id, user_id=user)


def create_user_like_featured(request, featured_id):
    user = request.user.pk
    return FeaturedLike.objects.create(featured_id=featured_id, user_id=user)


def register_user_in_event(request, event_id):
    user = request.user.pk
    return RegisterEvent.objects.filter(event_id=event_id, user_id=user)


def create_user_register_in_event(request, event_id):
    user = request.user.pk
    return RegisterEvent.objects.create(event_id=event_id, user_id=user)
