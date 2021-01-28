from django.db import models

# Create your models here.

from django.db import models
from colorfield.fields import ColorField

# Create your models here.
SKILL_CHOICES = (
            ('P', 'Programming'),
            ('TE', 'Technologies'),
            ('TO', 'Tools'),
        )

COLOR_CHOICES = (
            ('red', 'RED'),
            ('pink', 'PINK'),
            ('purple', 'PURPLE'),
            ('indigo', 'INDIGO'),
            ('blue', 'BLUE'),
            ('light-blue', 'LIGHT BLUE'),
            ('cyan', 'CYAN'),
            ('tael', 'TEAL'),
            ('green', 'GREEN'),
            ('light-green', 'LIGHT GREEN'),
            ('yellow', 'YELLOW'),
            ('amber', 'AMBER'),
            ('orange', 'ORANGE'),
            ('deep-orange', 'DEEP ORANGE'),
            ('brown', 'BROWN'),
            ('grey', 'GREY'),
            ('blue-grey', 'BLUE GREY'),
            ('black', 'BLACK'),
)

GRADE_CHOICES = (
            ('C', 'CGPA'),
            ('P', 'PERCENTILE'),
            ('G', 'GPA'),
)

ICON_CHOICES = (
    ('fab fa-python', 'python'),
    ('fab fa-js', 'js'),
    ('fab fa-css3-alt', 'css'),
    ('fab fa-html5', 'html5'),
    ('fas fa-file-code', 'C++'),
    ('fas fa-file-code', 'others'),
)


class Education(models.Model):
    degree_title = models.TextField(unique=True, max_length=500)
    university_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=5, choices=GRADE_CHOICES)

    def __str__(self):
        return f"{self.degree_title}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    skill_type = models.CharField(choices=SKILL_CHOICES, blank=True, max_length=3)
    level = models.IntegerField(blank=True, null=True)
    icon = models.CharField(choices=ICON_CHOICES, blank=True, max_length=30)
    color = ColorField(blank=True, null=True)

    def __str__(self):
        return f"skill: {self.name}"


class Hobby(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"skill: {self.name}"


class Achievement(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
            return f"{self.title}"


class Project(models.Model):
    title = models.CharField(max_length=30)
    technologies = models.TextField(blank=True, null=True)
    features = models.TextField()
    thumbnail = models.ImageField(blank=False, null=True)
    card_color = models.CharField(choices=COLOR_CHOICES, max_length=20, blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"

