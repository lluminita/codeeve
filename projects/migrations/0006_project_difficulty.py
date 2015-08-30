# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150830_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='difficulty',
            field=models.CharField(default=datetime.datetime(2015, 8, 30, 18, 23, 59, 278243, tzinfo=utc), max_length=2, choices=[(b'beginner', b'beginner'), (b'intermediate', b'intermediate'), (b'advanced', b'advanced')]),
            preserve_default=False,
        ),
    ]
