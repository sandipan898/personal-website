from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Article
from django.views.generic import DetailView
from django.urls import reverse
from .forms import ArticlePostForm, SignUpUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.


def home_view(request):
    template_name = 'blog/home.html'
    articles = Article.objects.filter(featured=True)

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


def signup_view(request):
    form = SignUpUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.email = form.cleaned_data.get('bio')
        user.profile.email = form.cleaned_data.get('image')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpUserForm()
    return render(request, 'signup.html', {'form': form})