# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150826_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='coach',
            field=models.ForeignKey(related_name='coach_of_projects', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
