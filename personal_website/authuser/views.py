from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import SignupUserForm
from .models import UserProfile
from django.contrib.auth import login, authenticate
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.views import 
from django.contrib import messages

from .forms import SignupUserForm, UserLoginForm

# from allauth.account.forms import LoginForm

# Create your views here.

class UserSignupView(generic.CreateView):
    form_class = SignupUserForm
    template_name = "authuser/signup.html"
    success_url = reverse_lazy('user-login')
    
    def get(self, request, *args, **kwargs):
        form = SignupUserForm()
        context={'form': form, 'next': str(request.GET.get('next'))}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        try:
            next_path = str(request.get_full_path()).split('next=')[1]
            if next_path is 'None' or '':
                next_path = '/'
        except Exception as e:
            next_path = '/'
        print(next_path)
        form = SignupUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            login(request, user)
            return redirect(next_path)
        else:
            print(form.errors)
            context = {'form': SignupUserForm(request.POST), 'errors': form.errors}
            return render(request, template_name=self.template_name, context=context)

class UserLoginView(LoginView):
    template_name="authuser/login.html"
    authentication_form=UserLoginForm
    redirect_field_name='next'
    context = {}

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        print(request.GET.get('next'))
        context={'form': form, 'next': request.GET.get('next')}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    next_path = str(request.get_full_path()).split('next=')[1]
                    print(next_path)
                    return redirect(next_path)
                except Exception as e:
                    print(e)
                    return redirect('/')
            else:
                messages.error(request, "This User is Inactive");
                self.context['error_msg'] = 'This User is Inactive'
        else:
            messages.error(request, "User does not exist!")
            self.context['error_msg'] = 'User does not exist'
        return render(request, template_name=self.template_name, context=self.context)
        
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
