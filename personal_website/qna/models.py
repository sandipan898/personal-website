from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class FAQ(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    is_answered = models.BooleanField(default=False, blank=True, null=True)
    published = models.BooleanField(default=False, blank=True, null=True)
    tags = TaggableManager(blank=True)
    upvotes = models.IntegerField(default=0, blank=True, null=True)
    downvotes = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.question