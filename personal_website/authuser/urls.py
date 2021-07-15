from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ( UserSignupView, UserProfileView, UserLoginView )
from .forms import  UserLoginForm

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('signup', UserSignupView.as_view(), name='user-signup-with-param'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]