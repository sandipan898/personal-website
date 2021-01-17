from django.urls import path
from .views import home_view, article_list_view, post_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('articles/', article_list_view, name='article-list'),
    path('articles/detail/', post_detail_view, name='article-detail'),
]