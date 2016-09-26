# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20160818_0346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pub_date',
            new_name='publication_date',
        ),
    ]
