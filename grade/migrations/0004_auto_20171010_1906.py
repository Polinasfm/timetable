# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0003_remove_disciplina_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscMinistrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('cod_prof', models.CharField(max_length=12)),
                ('disc_p', models.ManyToManyField(to='grade.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cod_turma', models.CharField(max_length=12)),
                ('disc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.DiscMinistrada')),
            ],
        ),
        migrations.AddField(
            model_name='discministrada',
            name='profId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.Professor'),
        ),
    ]
