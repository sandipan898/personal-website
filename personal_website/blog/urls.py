from django.urls import path
from .views import home_view, article_list_view, post_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('article/all/', article_list_view, name='article-list'),
    path('article/<int:id>/detail/', post_detail_view, name='article-detail'),
]