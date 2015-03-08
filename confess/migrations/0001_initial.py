# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(default=b'')),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default=b'', max_length=255, blank=True)),
                ('total_likes', models.IntegerField(default=b'0', blank=True)),
                ('category', models.CharField(blank=True, max_length=2, choices=[(b'PO', b'popular'), (b'NE', b'new'), (b'SE', b'sex'), (b'CO', b'college'), (b'RA', b'random')])),
            ],
            options={
                'ordering': ['-posted', 'title'],
            },
            bases=(models.Model,),
        ),
    ]
