from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from web_project.techreview.forms import CreateFeaturedForm
from web_project.techreview.models import Featured


class AllFeaturedView(views.ListView):
    context_object_name = 'featureds'
    model = Featured
    template_name = 'featured/all-featured.html'
    # template_name = 'event/test.html'



class CreateFeaturedView(views.CreateView):
    template_name = 'featured/create-featured.html'
    form_class = CreateFeaturedForm

    # TODO: CHANGE TO EVENT DETAILS
    # success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = CreateFeaturedForm(request.POST, request.FILES)
        if form.is_valid():
            featured = form.save(commit=False)
            featured.user = request.user
            featured.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        return render(request, 'featured/create-featured.html', {'form': form})
