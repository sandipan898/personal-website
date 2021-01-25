from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ( UserSignupView )

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('login/', LoginView.as_view(template_name="authuser/login.html"), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
]