from django.urls import reverse_lazy
from django.views import generic as views

from web_project.accounts.models import Profile


class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    extra_context = {'title': 'Template view'}


