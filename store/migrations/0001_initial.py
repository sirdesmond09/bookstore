# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length= 200)),
                ('description', models.TextField()),
                ('date_posted', models.DateField(default = timezone.now)),
                ('price', models.DecimalField(decimal_places= 2, max_digits= 8)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
