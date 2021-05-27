from django.urls import path
from .views import (
    HomeView, QuestionDetailView, create_question_view,
    question_list_view, change_votes
)

urlpatterns = [
    path('', HomeView.as_view(), name='qna-home'),
    path('question/all', question_list_view, name='qna-list'),
    path('question/detail/<slug:slug>/', QuestionDetailView.as_view(), name='qna-detail'),
    path('question/create/', create_question_view, name='qna-create'),  
    path('question/change-vote/', change_votes, name='change-vote'),  
]