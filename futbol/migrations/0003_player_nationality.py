# Generated by Django 5.0.4 on 2024-04-19 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0002_rename_id_team_puntos_equipo_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='nationality',
            field=models.CharField(default='Desconocido', max_length=100),
        ),
    ]