# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confess', '0004_post_liked'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MtmLike2Conf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confession', models.ForeignKey(to='confess.Post')),
                ('like', models.ForeignKey(to='likes.Like')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
