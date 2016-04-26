# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import rango.models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=rango.models.user_pic_upload_path, blank=True),
        ),
    ]
