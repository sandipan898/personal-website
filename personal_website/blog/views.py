from django import views
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Article, get_all_related_topic, Comment, Reply
from .forms import ArticlePostForm, CommentForm

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
    related_topics = get_all_related_topic()

    context = {
        "articles": articles,
        "related_topics": related_topics
    }
    return render(request, template_name=template_name, context=context)  
  
def post_detail_view(request, slug):
    context = {}
    template_name = 'blog/detail-page.html'
    selected_article = get_object_or_404(Article, slug=slug)
    related_articles = Article.objects.all()
    comments = Comment.objects.filter(article=selected_article)

    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_comment = Comment.objects.create(
                article=selected_article,
                comment_author=form.cleaned_data['comment_author'], 
                comment_body = form.cleaned_data['comment_body'],
            )
            new_comment.save()
            messages.success(request, "Comment posted!")
            return redirect('article-home')
    else:
        form = CommentForm()
        context['form'] = form
        
    return render(request, context={'article': selected_article, 'related_articles': related_articles, 'comments': comments}, template_name=template_name)


class PostDetailView(views.View):
    template_name = 'blog/detail-page.html'
    context = {}
    
    def get(self, *args, **kwargs):
        selected_article = get_object_or_404(Article, slug=kwargs['slug'])
        related_articles = Article.objects.all()
        comments = Comment.objects.filter(article=selected_article)
        form = CommentForm()
        self.context['form'] = form

        context = {
            'article': selected_article,
            'related_articles': related_articles, 
            'comments': comments,
            'comment_count': comments.count()
        }
        
        self.context.update(context)
        return render(self.request, self.template_name, context=self.context)
    
    # @login_required(login_url='/auth/login/')
    def post(self, *args, slug, **kwargs):
        
        # if self.request.user == 'AnonymousUser':
        #     return redirect('user-login')
        
        form = CommentForm(self.request.POST)     
        selected_article = get_object_or_404(Article, slug=slug)
        print(selected_article)
        if form.is_valid():

            new_comment = Comment.objects.create(
                article=selected_article,
                comment_author=form.cleaned_data['comment_author'], 
                # comment_author = self.request.user.full_name,
                comment_body = form.cleaned_data['comment_body'],
            )        
            new_comment.save()
            messages.success(self.request, "Comment posted!")
            return redirect('/blog/article/detail/'+slug)

        else:
            print("Please fill the form correctly")
            messages.warning(self.request, "Please fill the form correctly");
            return redirect('article-detail')


@login_required(login_url='/auth/login/')
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
            messages.success(request, "Post will be published Soon!")
            return redirect('article-home')
    else:
        form = ArticlePostForm()
        context['form'] = form
    
    return render(request, template_name, context=context)
