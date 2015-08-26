# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20150826_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='coach',
        ),
        migrations.AddField(
            model_name='project',
            name='coach',
            field=models.ForeignKey(null=True, related_name='coach_of_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
