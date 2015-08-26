# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150826_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='coach',
            field=models.ManyToManyField(related_name='coach_of_projects', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
