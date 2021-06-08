from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from .forms import SignupUserForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class UserSignupView(generic.CreateView):
    form_class = SignupUserForm
    template_name = "authuser/signup.html"
    success_url = reverse_lazy('user-login')

    # def get(self, request, *args):
    #     print("User Signup")
    #     return render(self.request, template_name=self.template_name)


class UserLoginView(LoginView):
    template_name="authuser/login.html"
    authentication_form=UserLoginForm

    # def get_success_url(self):
    #     print(self.request.GET['next'])


# class UserLoginView(LoginView):
    # def post(self, request, *args, **kwargs):
        # if request.get_full_path()