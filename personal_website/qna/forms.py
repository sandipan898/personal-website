from django import forms 
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.forms import fields
from .models import Question, Answer


class QuestionPostForm(forms.ModelForm):
    title = forms.CharField(
        label="Question Title",
        max_length=400,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    body = forms.CharField(
        label="Question Body",
        max_length=2000,
        widget=CKEditorWidget()
    )
    tags = forms.CharField(
        required=False,
        label="Enter Tags related to your Question Topic",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )

    class Meta:
        model = Question
        fields = [
            "title",
            "body",
            "tags",
        ]


class AnswerPostForm(forms.ModelForm):
    author = forms.CharField(
        label="Your Name",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    body = forms.CharField(
        label="Answer Body",
        max_length=2000,
        widget=CKEditorWidget()
    )

    class Meta:
        model = Answer
        fields = [
            "author",
            "body",
        ]

