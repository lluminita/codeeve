# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='difficulty',
            field=models.CharField(max_length=15, choices=[(b'beginner', b'beginner'), (b'intermediate', b'intermediate'), (b'advanced', b'advanced')]),
        ),
    ]
