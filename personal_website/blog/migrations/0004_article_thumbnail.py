# Generated by Django 3.1.5 on 2021-01-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210110_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
