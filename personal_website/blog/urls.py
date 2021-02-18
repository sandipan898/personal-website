from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
        home_view, 
        article_list_view, 
        post_detail_view, 
        create_article_view, 
        PostDetailView
)

urlpatterns = [
    path('', home_view, name='article-home'),
    path('article/all', article_list_view, name='article-list'),
    path('article/detail/<slug:slug>/', PostDetailView.as_view(), name='article-detail'),
    path('article/create/', create_article_view, name='create-article'),
]