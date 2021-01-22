from django import forms 
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import Article

# class ArticlePostForm(forms.Form):
#     topic_related_to = forms.CharField(max_length=400)
#     title = forms.CharField(max_length=200)
#     content = RichTextField()
#     tags = forms.CharField(max_length=100)
#     thumbnail = forms.ImageField()

class ArticlePostForm(forms.ModelForm):
    topic_related_to = forms.CharField(
        label='topic_related_to', 
        max_length=400,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    title = forms.CharField(
        label="title",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    content = forms.CharField(
        label="title",
        max_length=200,
        widget=CKEditorWidget()
    )
    tags = forms.CharField(
        label="tags",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    thumbnail = forms.ImageField()

    class Meta:
        model = Article
        fields = [
            "topic_related_to",
            "title",
            "content",
            "tags",
            "thumbnail",
        ]