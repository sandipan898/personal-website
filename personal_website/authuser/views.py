from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

from .forms import SignupUserForm, UserLoginForm
# from allauth.account.forms import LoginForm

# Create your views here.

class UserSignupView(generic.CreateView):
    form_class = SignupUserForm
    template_name = "authuser/signup.html"
    success_url = reverse_lazy('user-login')

    # def get(self, request, *args):
    #     print("User Signup")
    #     return render(self.request, template_name=self.template_name)


# class UserLoginView(LoginView):
#     template_name="authuser/login.html"
#     authentication_form=UserLoginForm


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
