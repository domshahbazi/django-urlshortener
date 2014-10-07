# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urlObj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_url', models.CharField(max_length=200)),
                ('short_url', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(verbose_name=b'Date Created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
