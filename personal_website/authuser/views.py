from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import SignupUserForm
from .models import UserProfile
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


class UserProfileView(generic.View):
    def get(self, request, *args, **kwargs):
        template_name = 'authuser/userprofile.html'
        user = UserProfile(user=request.user)
        print(user)
        user_data = {
            "username": user.user.username,
            "first_name": user.user.first_name,
            "last_name": user.user.last_name,
            "email":user.user.email,
            "bio":user.bio,
            'password1':user.user.password,
            "image":user.image,
        }
        form_data = SignupUserForm(
            initial=user_data
        )
        # print(form_data)
        return render(request, template_name=template_name, context={'form_data': form_data})
    
    def post(self, request, *args, **kwargs):
        post_data = SignupUserForm(data=request.POST,)
        if post_data.is_valid():
            print("Valid!")
            user = UserProfile.objects.get(
                user__username=request.user.username,
            )
            updated_user = user.objects.update(
                user__username=post_data.cleaned_data['username'],
                user__first_name=post_data.cleaned_data['first_name'],
                user__last_name=post_data.cleaned_data['last_name'],
                user__email=post_data.cleaned_data['email'],
                bio=post_data.cleaned_data['bio'],
                user__password=post_data.cleaned_data['password1'],
                image=post_data.cleaned_data['image'],
            )
            print(updated_user)
            updated_user.save()
        print(post_data.errors)
        print("User")
        return redirect('user-profile')
