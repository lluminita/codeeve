# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_create_project_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 11, 20, 21, 58, 47, 657721, tzinfo=utc), upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='difficulty',
            field=models.CharField(max_length=15, choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced')]),
        ),
    ]
