# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-13 02:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recurso',
            old_name='descripccion',
            new_name='descripcion',
        ),
        migrations.AlterField(
            model_name='artefacto',
            name='cargado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]