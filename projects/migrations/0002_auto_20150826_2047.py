# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('max_members', models.IntegerField()),
                ('coach', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='coach_of_projects')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='owns_project')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='participant_of_projects')),
            ],
        ),
        migrations.RemoveField(
            model_name='projects',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='participants',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
