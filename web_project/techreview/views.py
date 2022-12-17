from django.contrib.auth import get_user_model

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from web_project.common.forms import FeaturedCommentForm
from web_project.common.models import FeaturedLike, FeaturedComment
from web_project.core.other_validators import user_liked_featured
from web_project.core.permissions_mixin import PermissionMixin
from web_project.techreview.utils import get_featured_id_from_slug
from web_project.techreview.forms import CreateFeaturedForm, EditFeaturedForm
from web_project.techreview.models import Featured

UserModel = get_user_model()


class CreateFeaturedView(PermissionMixin, views.CreateView):
    template_name = 'featured/create-featured.html'
    form_class = CreateFeaturedForm

    def post(self, request, *args, **kwargs):
        form = CreateFeaturedForm(request.POST, request.FILES)
        if form.is_valid():
            featured = form.save(commit=False)
            featured.user = request.user
            featured.save()
            return HttpResponseRedirect(reverse_lazy('all featured'))
        return render(request, 'featured/create-featured.html', {'form': form})


class AllFeaturedView(views.ListView):
    context_object_name = 'featureds'
    model = Featured
    template_name = 'featured/all-featured.html'


class EditFeaturedView(PermissionMixin, views.UpdateView):
    model = Featured
    template_name = 'featured/edit-featured.html'
    form_class = EditFeaturedForm
    slug_url_kwarg = 'slug'

    success_url = reverse_lazy('all featured')


class DeleteFeaturedView(PermissionMixin, views.DeleteView):
    model = Featured
    template_name = 'featured/delete-featured.html'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('all featured')


class DetailsFeaturedView(views.DetailView):
    model = Featured
    template_name = 'featured/details-featured.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        form = FeaturedCommentForm(instance=self.request.user)
        user_name = UserModel.objects.filter(email=self.request.user).get()
        current_slug = self.kwargs.get(self.slug_url_kwarg)
        current_featured = get_featured_id_from_slug(current_slug).pk
        comment_count = FeaturedComment.objects.filter(featured_id=current_featured).count()
        likes_count = FeaturedLike.objects.filter(featured_id=current_featured).count()

        data = super().get_context_data(**kwargs)
        data['comment_form'] = form
        data['user_name'] = user_name
        data['user_is_like'] = user_liked_featured(self.request, current_featured)
        data['comment_count'] = comment_count
        data['likes_count'] = likes_count
        return data
