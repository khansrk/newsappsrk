# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='is_active',
        ),
        migrations.AddField(
            model_name='feed',
            name='status',
            field=models.CharField(default=1, max_length=1, choices=[(b'a', b'Active'), (b'n', b'Inactive'), (b'r', b'Rejected')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
