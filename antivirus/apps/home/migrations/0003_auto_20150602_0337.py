# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150602_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antivirus',
            name='imagen',
            field=models.ImageField(upload_to=b'ImgAntivirus'),
        ),
    ]
