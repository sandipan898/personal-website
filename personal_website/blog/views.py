from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article
from django.views.generic import DetailView
from django.urls import reverse
from .forms import ArticlePostForm

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
  
def post_detail_view(request, slug):
    template_name = 'blog/detail-page.html'
    # queryset = Article.objects.filter(slug=slug)
    selected_article = get_object_or_404(Article, slug=slug)
    related_articles = Article.objects.all()
    return render(request, context={'article': selected_article, 'related_articles': related_articles}, template_name=template_name)


class CreateArticleView(generic.CreateView):
    template_name = 'blog/article_form.html'
    form_class = ArticlePostForm