# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confess', '0003_remove_post_is_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
