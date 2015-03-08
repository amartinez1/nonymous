# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_token', models.CharField(max_length=100)),
                ('vote', models.SmallIntegerField(choices=[(1, b'+1'), (-1, b'-1'), (0, b'0')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('liked', models.BooleanField(default=False)),
                ('label', models.CharField(max_length=30)),
                ('post', models.ForeignKey(to='confess.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('user_token', 'post')]),
        ),
    ]
