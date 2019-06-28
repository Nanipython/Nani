# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('product_number', models.IntegerField()),
                ('product_name', models.CharField(max_length=25)),
                ('product_cost', models.IntegerField()),
                ('product_class', models.CharField(max_length=20)),
                ('product_weight', models.IntegerField()),
            ],
        ),
    ]
