from .models import  UserProfile
from django import forms 
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.password_validation import password_validators_help_text_html
from django.contrib.auth.models import User

class SignupUserForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
        }))
    first_name = forms.CharField(label="First name", max_length=100, 
                widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
        })
    )
    last_name = forms.CharField(label="Last name", max_length=100, widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
                }))
    username = UsernameField(widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
                }))
    bio = forms.CharField(label="Bio", max_length=400, widget=forms.Textarea(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
                }))
    
    password1 = forms.CharField(
                    label="Password",
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
                    'autocomplete': 'new-password',
                    }), help_text=password_validators_help_text_html()
                )
    password2 = forms.CharField(
                    label="Re-enter Password",
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
                    'autocomplete': 'new-password',
                    }), help_text=("Enter the same password as before, for verification.")
                )
    image = forms.ImageField(allow_empty_file=True)


    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "bio",
            "password1",
            "password2",
            "image"
        ]
        
        def clean_username(self):
            username = self.cleaned_data['username']
            if len(username) < 2:
                raise forms.ValidationError("Username is too short")
            elif User.objects.get_object_or_404(username=username):
                raise forms.ValidationError("This username is already taken")
            return username
