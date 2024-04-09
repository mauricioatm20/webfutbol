# Generated by Django 5.0.4 on 2024-04-10 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='logos')),
                ('total_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='puntos_equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jornada', models.PositiveIntegerField(verbose_name='Jornada')),
                ('puntos', models.PositiveIntegerField(verbose_name='Puntos')),
                ('id_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbol.teams')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('position', models.CharField(max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbol.teams')),
            ],
        ),
        migrations.CreateModel(
            name='PartidoResultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goles_local', models.PositiveIntegerField(default=0, verbose_name='Goles equipo local')),
                ('goles_visitante', models.PositiveIntegerField(default=0, verbose_name='Goles equipo visitante')),
                ('equipo_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_local', to='futbol.teams', verbose_name='Equipo local')),
                ('equipo_visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_visitante', to='futbol.teams', verbose_name='Equipo visitante')),
            ],
        ),
    ]