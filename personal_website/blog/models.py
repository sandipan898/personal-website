from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from taggit.managers import TaggableManager

# Create your models here.

class Article(models.Model):
    author = OneToOneField(User, on_delete=models.CASCADE)
    topic_related_to = models.CharField(max_length=400, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    # is_publishable = models.BooleanField(default=False, blank=True, null=True)
    published = models.BooleanField(default=False, blank=True, null=True)
    tags = TaggableManager()
    
    def __str__(self):
        return "Article {} of Author {}".format(self.title, self.author)


