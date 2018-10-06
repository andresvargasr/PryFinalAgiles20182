# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-06 07:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area_usuaria',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Artefacto',
            fields=[
                ('id_artefacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_mostrar', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('archivo', models.FileField(null=True, upload_to='files')),
                ('fecha_hora_carga', models.DateTimeField()),
                ('fecha_hora_edicion', models.DateTimeField(null=True)),
                ('reusable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Dueno',
            fields=[
                ('id_dueno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=150)),
                ('apellido', models.CharField(blank=True, max_length=150)),
                ('cargo', models.CharField(blank=True, max_length=150)),
                ('celular', models.CharField(blank=True, max_length=10)),
                ('id_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.Area_usuaria')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id_proyecto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=150)),
                ('descripcion', models.CharField(blank=True, max_length=1000)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('id_dueno_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.Dueno')),
                ('id_responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id_recurso', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('tipo', models.CharField(max_length=150)),
                ('descripccion', models.CharField(max_length=1000)),
                ('ubicacion', models.CharField(blank=True, max_length=1000)),
                ('fecha_creacion', models.DateField()),
                ('reusable', models.BooleanField(default=False)),
                ('id_proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='images')),
                ('country', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recurso',
            name='id_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.Usuario'),
        ),
        migrations.AddField(
            model_name='artefacto',
            name='cargado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.Usuario'),
        ),
        migrations.AddField(
            model_name='area_usuaria',
            name='id_departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.Departamento'),
        ),
    ]
