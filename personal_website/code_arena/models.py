from django.db import models

# Create your models here.

class Code(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title