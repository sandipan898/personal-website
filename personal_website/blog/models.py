from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class ArticleUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_related_to = models.CharField(max_length=400, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    published = models.BooleanField(default=False, blank=True, null=True)
    tags = TaggableManager()
    upvotes = models.IntegerField(default=0, blank=True, null=True)
    downvotes = models.IntegerField(default=0, blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='')
    published_on = models.DateField(auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return "Article \"{}\" of Author {}".format(self.title, self.author)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={
            'slug': self.slug
        })

    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, blank=True, null=True)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE) 
    comment_body = models.TextField(blank=True, null=True)
    upvotes = models.IntegerField(default=0, blank=True, null=True)
    downvotes = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return "comment {} of article {}".format(self.id, self.article.title)
        