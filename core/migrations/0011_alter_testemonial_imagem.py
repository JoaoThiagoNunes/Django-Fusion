# Generated by Django 4.2.1 on 2023-05-23 13:42

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_testemunha1_testemonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testemonial',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 75, 'width': 75}}, verbose_name='Imagem'),
        ),
    ]
