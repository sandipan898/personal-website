# Generated by Django 3.1.5 on 2021-01-17 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]