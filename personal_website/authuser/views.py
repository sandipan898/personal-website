from django.shortcuts import render, HttpResponse, redirect
# from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.views import generic
from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import 
from django.contrib import messages

from .models import UserProfile
from .forms import SignupUserForm, UserLoginForm, EditUserForm

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
            if next_path == 'None' or next_path == '':
                next_path = '/'
        except Exception as e:
            next_path = '/'
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
        # user_data = {
        #     "username": user.user.username,
        #     "first_name": user.user.first_name,
        #     "last_name": user.user.last_name,
        #     "email":user.user.email,
        #     "bio":user.bio,
        #     "image":user.imageURL
        # }
        form_data = EditUserForm(instance=user.user)
        return render(request, template_name=template_name, context={'form_data': form_data})
    
    def post(self, request, *args, **kwargs):
        userprofile = UserProfile.objects.get(
            user=request.user,
        )
        post_data = EditUserForm(request.POST, request.FILES, instance=userprofile)
        if post_data.is_valid():
            print(post_data.cleaned_data)
            # updated_user.user.username=post_data.cleaned_data['username']
            userprofile.user.first_name=post_data.cleaned_data['first_name']
            # userprofile.user.last_name=post_data.cleaned_data['last_name']
            # userprofile.user.email=post_data.cleaned_data['email']
            # userprofile.bio=post_data.cleaned_data['bio']
            # userprofile.image=post_data.cleaned_data['image']
            updated_user = post_data.save()
            print(updated_user.user.first_name)
            updated_user.save()
        else:
            print(post_data.errors)
        return redirect('user-profile')

# class UserProfileView(generic.UpdateView):
#     model = UserProfile
#     fields = ["username",
#             "first_name",
#             "last_name",
#             "email",
#             "bio",
#             "image"] 
#     slug_field = 'username'
#     slug_url_kwarg = 'slug'
