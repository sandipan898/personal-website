from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.

def home_view(request):
    """ Home View """
    template_name = 'blog/home.html'
    return render(request, template_name=template_name)
