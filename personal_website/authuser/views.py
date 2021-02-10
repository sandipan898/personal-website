from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from .forms import SignupUserForm
from django.contrib.auth import login, authenticate
from django.views import generic

# Create your views here.

class UserSignupView(generic.CreateView):
    form_class = SignupUserForm
    template_name = "authuser/signup.html"
    success_url = reverse_lazy('user-login')

    # def get(self, request, *args):
    #     print("User Signup")
    #     return render(self.request, template_name=self.template_name)
