from django import forms 
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import Article, ArticleUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    bio = forms.CharField(max_length=400, help_text='Bio')
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio', 'password1', 'password2', 'image')


class ArticlePostForm(forms.ModelForm):
    title = forms.CharField(
        label="Post Title",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    content = forms.CharField(
        label="Post Content",
        max_length=200,
        widget=CKEditorWidget()
    )
    topic_related_to = forms.CharField(
        required=False,
        label='Post Topic related to', 
        max_length=400,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    tags = forms.CharField(
        required=False,
        label="Enter Tags related to your Post",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    thumbnail = forms.ImageField(required=False)

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "topic_related_to",
            "tags",
            "thumbnail",
        ]