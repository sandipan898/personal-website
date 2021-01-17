from django.shortcuts import render
from django.views import generic
from .models import Article
from django.views.generic import DetailView
from django.urls import reverse

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
    
# def post_detail_view(request, id):
#     print(id)
#     template_name = 'blog/detail-page.html'
#     return render(request, template_name=template_name)
    

class PostDetailView(DetailView):
    model = Article
    template_name = 'blog/detail-page.html'
    slug_url_kwarg = 'slug'
    # reverse('show_post', args=[the_post.slug])
post_detail_view = PostDetailView.as_view()
    