from django.shortcuts import render
from django.views.generic import View
from .models import Article

# Create your views here.


def home_view(request):
    template_name = 'blog/home.html'
    return render(request, template_name=template_name)
    