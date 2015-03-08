# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confess', '0002_post_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_liked',
        ),
    ]
