# from django.shortcuts import redirect, render
# from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views import generic as views

from web_project.common.forms import FeaturedCommentForm
from web_project.common.models import FeaturedLike
from web_project.common.uitls import get_current_url_path
from web_project.core.other_validators import user_liked_featured, create_user_like_featured, register_user_in_event, \
    create_user_register_in_event
from web_project.techreview.models import Featured

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'common/index.html'

    # extra_context = {'comment_form': FeaturedCommentForm()}

    def get_context_data(self, **kwargs):
        # featured = Featured.objects.all()
        user_verification = self.request.user
        if user_verification.is_authenticated:
            data = super().get_context_data(**kwargs)
            data['comment_form'] = FeaturedCommentForm(instance=self.request.user)
            # data['ss'] = FeaturedLike.objects.filter(featured_id=featured.i)
            return data


# class CommentFeatured(views.CreateView):
#     model = FeaturedComment
#     fields = ['text',]
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user

'''Second view for comments'''


# class FeaturedPostDetailView(views.DetailView):
#     model = FeaturedPost
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#
#         comments_connected = FeaturedComments.objects.filter(
#             post_connected=self.get_object()).order_by('-date_posted')
#         data['comments'] = comments_connected
#         if self.request.user.is_authenticated:
#             data['comment_form'] = NewCommentForm(instance=self.request.user)
#
#         return data
#
#     def post(self, request, *args, **kwargs):
#         new_comment = FeaturedComments(
#             content=request.POST.get('content'),
#             author=self.request.user,
#             post_connected=self.get_object())
#         new_comment.save()
#         return self.get(self, request, *args, **kwargs)
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