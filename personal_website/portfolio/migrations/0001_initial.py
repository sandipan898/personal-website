# Generated by Django 3.1.5 on 2021-01-26 18:21

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_title', models.TextField(max_length=500, unique=True)),
                ('university_name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(blank=True, max_length=100)),
                ('grade', models.CharField(choices=[('C', 'CGPA'), ('P', 'PERCENTILE'), ('G', 'GPA')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('technologies', models.TextField(blank=True, null=True)),
                ('modules', models.TextField(blank=True, null=True)),
                ('features', models.TextField()),
                ('front_icon', models.ImageField(null=True, upload_to='')),
                ('card_color', models.CharField(choices=[('red', 'RED'), ('pink', 'PINK'), ('purple', 'PURPLE'), ('indigo', 'INDIGO'), ('blue', 'BLUE'), ('light-blue', 'LIGHT BLUE'), ('cyan', 'CYAN'), ('tael', 'TEAL'), ('green', 'GREEN'), ('light-green', 'LIGHT GREEN'), ('yellow', 'YELLOW'), ('amber', 'AMBER'), ('orange', 'ORANGE'), ('deep-orange', 'DEEP ORANGE'), ('brown', 'BROWN'), ('grey', 'GREY'), ('blue-grey', 'BLUE GREY'), ('black', 'BLACK')], max_length=20)),
                ('visit_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_type', models.CharField(blank=True, choices=[('P', 'Programming'), ('TE', 'Technologies'), ('TO', 'Tools')], max_length=3)),
                ('skill_level', models.IntegerField(blank=True, null=True)),
                ('icon', models.CharField(blank=True, choices=[('fab fa-python', 'python'), ('fab fa-js', 'js'), ('fab fa-css3-alt', 'css'), ('fab fa-html5', 'html5'), ('fas fa-file-code', 'C++'), ('fas fa-file-code', 'others')], max_length=30)),
                ('color', colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='portfolio.project')),
            ],
        ),
    ]