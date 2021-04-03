from django import forms 
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.forms import fields
from .models import Article, Comment, Reply


class CommentForm(forms.ModelForm): 
    comment_author = forms.CharField(
        label="Your Name",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )

    comment_body = forms.CharField(
        label="Comment Body",
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
        })
    )
    

    class Meta:
        model = Comment
        fields = ['comment_author', 'comment_body']


class ReplyForm(forms.ModelForm): 
    reply_body = forms.CharField(
        label="Reply Body",
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
        })
    )

    class Meta:
        model = Comment
        fields = ['comment_body']


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