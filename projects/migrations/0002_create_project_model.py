# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('max_members', models.IntegerField()),
                ('difficulty', models.CharField(max_length=15, choices=[(b'beginner', b'beginner'), (b'intermediate', b'intermediate'), (b'advanced', b'advanced')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('coach', models.ForeignKey(related_name='coach_of_projects', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(related_name='owns_project', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='participant_of_projects', to=settings.AUTH_USER_MODEL, blank=True)),
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
