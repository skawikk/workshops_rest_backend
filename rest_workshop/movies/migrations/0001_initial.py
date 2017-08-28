# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('year', models.IntegerField(blank=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoviesStarringPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=128, null=True)),
                ('starring_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='moviesstarringperson',
            name='starring_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_name', to='movies.Person'),
        ),
        migrations.AddField(
            model_name='movies',
            name='actors',
            field=models.ManyToManyField(related_name='movie_person', through='movies.MoviesStarringPerson', to='movies.Person'),
        ),
        migrations.AddField(
            model_name='movies',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.Person'),
        ),
    ]