from django.contrib import admin
from .models import Article, Comment, ArticleUser

# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(ArticleUser)

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
