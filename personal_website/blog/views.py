from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Article
from django.views.generic import DetailView
from django.urls import reverse
from .forms import ArticlePostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    articles = Article.objects.all()

    context = {
        "articles": articles
    }
    return render(request, template_name=template_name, context=context)  
  
def post_detail_view(request, slug):
    template_name = 'blog/detail-page.html'
    # queryset = Article.objects.filter(slug=slug)
    selected_article = get_object_or_404(Article, slug=slug)
    related_articles = Article.objects.all()
    return render(request, context={'article': selected_article, 'related_articles': related_articles}, template_name=template_name)


@login_required
def create_article_view(request):
    template_name = 'blog/article_form.html'
    context = {}
    if request.method == "POST":
        form = ArticlePostForm(request.POST, request.FILES or None)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new_article = Article.objects.create(
                author=request.user, 
                topic_related_to = form.cleaned_data['topic_related_to'],
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                tags = form.cleaned_data['tags'],
                thumbnail = form.cleaned_data.get('thumbnail'),
            )
            new_article.save()
            messages.success(request, ("Post will be published Soon!"))
            return redirect('home')
    else:
        form = ArticlePostForm()
        context['form'] = form
    
    return render(request, template_name, context=context)
