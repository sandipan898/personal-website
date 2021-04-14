from django.urls import path
from .views import (
    HomeView, QuestionDetailView, create_question_view,
    question_list_view,
)

urlpatterns = [
    path('', HomeView.as_view(), name='qna-home'),
    path('article/all', question_list_view, name='qna-list'),
    path('question/detail/<slug:slug>/', QuestionDetailView.as_view(), name='qna-detail'),
    path('question/create/', create_question_view, name='qna-question'),  
]