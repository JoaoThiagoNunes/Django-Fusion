# Generated by Django 4.2.1 on 2023-05-23 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_plano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plano',
            name='titulo',
        ),
    ]
