# Generated by Django 3.1.5 on 2021-01-23 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210123_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
