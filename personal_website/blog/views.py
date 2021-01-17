from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.


def home_view(request):
    template_name = 'blog/home.html'
    articles = Article.objects.all()

    context = {
        "articles": articles
    }
    return render(request, context=context, template_name=template_name)
    
def article_list_view(request):
    template_name = 'blog/article-list.html'
    return render(request, template_name=template_name)
    
def post_detail_view(request):
    template_name = 'blog/detail-page.html'
    return render(request, template_name=template_name)
    
