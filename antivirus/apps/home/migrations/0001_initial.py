# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='antivirus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False)),
                ('descripcion', models.CharField(max_length=150)),
                ('imagen', models.ImageField(upload_to=b'events')),
                ('precio', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('SistemaOperativo', models.CharField(max_length=60)),
                ('arquitectura', models.CharField(max_length=60)),
                ('ram', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='antivirus',
            name='categoria',
            field=models.ForeignKey(to='home.Categoria'),
        ),
    ]
