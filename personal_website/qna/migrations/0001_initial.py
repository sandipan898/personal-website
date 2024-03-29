# Generated by Django 3.1.5 on 2021-04-14 09:41

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('is_answered', models.BooleanField(blank=True, default=False, null=True)),
                ('published', models.BooleanField(blank=True, default=False, null=True)),
                ('upvotes', models.IntegerField(blank=True, default=0, null=True)),
                ('downvotes', models.IntegerField(blank=True, default=0, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('published', models.BooleanField(blank=True, default=False, null=True)),
                ('upvotes', models.IntegerField(blank=True, default=0, null=True)),
                ('downvotes', models.IntegerField(blank=True, default=0, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qna.question')),
            ],
        ),
    ]
