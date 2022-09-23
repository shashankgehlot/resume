from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import get_object_or_404

from .models import GeeksModel

class GeeksListView(ListView):
    # specify the model to use
    model = GeeksModel
    template_name = 'base.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(GeeksModel, slug=self.kwargs['slug'])
        return GeeksModel.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self,*args, **kwargs):
        # context = super(GeeksModel, self).all(*args, **kwargs)
        context ={}
        context['user'] = GeeksModel.objects.filter(slug=self.kwargs['slug'])
        return context


