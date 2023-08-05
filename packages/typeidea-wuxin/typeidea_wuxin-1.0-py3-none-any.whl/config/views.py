from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from blog.views import CommonViewMixin
from .models import Links
# Create your views here.

class LinkView(CommonViewMixin, ListView):
    queryset = Links.objects.filter(status=Links.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'