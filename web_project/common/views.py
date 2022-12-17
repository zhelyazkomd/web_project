from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import generic as views

from web_project.common.forms import FeaturedCommentForm

from web_project.common.uitls import get_current_url_path
from web_project.core.other_validators import user_liked_featured, create_user_like_featured, register_user_in_event, \
    create_user_register_in_event
from web_project.techreview.models import Featured

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        user_verification = self.request.user
        if user_verification.is_authenticated:
            data = super().get_context_data(**kwargs)
            data['comment_form'] = FeaturedCommentForm(instance=self.request.user)

            return data


@login_required
def comment_featured(request, featured_id):
    featured = Featured.objects.filter(pk=featured_id).get()
    current_user = request.user.id
    form = FeaturedCommentForm(request.POST)
    user = UserModel.objects.filter(pk=current_user).get()

    if form.is_valid():
        comment = form.save(commit=False)
        comment.featured = featured
        comment.user = user
        comment.save()

    return redirect(get_current_url_path(request))


@login_required
def like_featured(request, featured_id):
    liked_featured_by_user = user_liked_featured(request, featured_id)
    if liked_featured_by_user:
        liked_featured_by_user.delete()
    else:
        create_user_like_featured(request, featured_id)
    return redirect(get_current_url_path(request))


def register_event(request, event_id):
    registered = register_user_in_event(request, event_id)

    if registered:
        registered.delete()
    else:
        create_user_register_in_event(request, event_id)

    return redirect(get_current_url_path(request))


class AboutUsView(views.TemplateView):
    template_name = 'common/about_us.html'


def handler404(request, *args, **kwargs):
    context = {}
    template_name = 'errors/404.html'
    response = render(request, template_name=template_name, context=context)
    response.status_code = 404
    return response


def handler500(request, *args, **kwargs):
    context = {}
    template_name = 'errors/500.html'
    response = render(request, template_name=template_name, context=context)
    response.status_code = 500
    return response
