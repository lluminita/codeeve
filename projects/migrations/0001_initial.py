# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('max_members', models.IntegerField()),
                ('owner', models.ForeignKey(related_name='owns_project', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='participant_of_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
