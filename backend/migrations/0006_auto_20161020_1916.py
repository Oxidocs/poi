# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20161019_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=500)),
                ('lugares', models.ManyToManyField(to='backend.Lugares')),
            ],
            options={
                'verbose_name_plural': 'Circuitos',
            },
        ),
        migrations.CreateModel(
            name='Subcategorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=500)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Categorias')),
            ],
            options={
                'verbose_name_plural': 'Sub Categorias',
            },
        ),
        migrations.RemoveField(
            model_name='rutas',
            name='lugares',
        ),
        migrations.AddField(
            model_name='rutas',
            name='ciudad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.Ciudades'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuitos',
            name='ruta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Rutas'),
        ),
    ]
