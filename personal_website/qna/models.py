from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

from authuser.models import UserProfile
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=400, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    featured = models.BooleanField(default=False, blank=True, null=True)
    is_answered = models.BooleanField(default=False, blank=True, null=True)
    published = models.BooleanField(default=False, blank=True, null=True)
    published_on = models.DateField(auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    answer_count = models.IntegerField(default=0, blank=True, null=True)
    tags = TaggableManager(blank=True)
    upvotes = models.IntegerField(default=0, blank=True, null=True)
    downvotes = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("qna-detail", kwargs={
            'slug': self.slug, 
            # 'id': self.id
        })
    
    @property
    def get_answer_count(self):
        """Called every time when a Answer will be saved"""
        print(self)
        try:
            answers = Answer.objects.filter(question=self)
            self.answer_count = answers.count()
        except Exception as e:
            print(e)

class Answer(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False, blank=True, null=True)
    upvotes = models.IntegerField(default=0, blank=True, null=True)
    downvotes = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.question.title


def get_all_related_topic(): 
    questions = Question.objects.all()
    related_topics = []
    for question in questions:
        related_topics.append(question.tags)

    return related_topics
