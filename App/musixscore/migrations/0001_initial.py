# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(


            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(

            name='Performer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=50, null=True)),
                ('lname', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('age', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
