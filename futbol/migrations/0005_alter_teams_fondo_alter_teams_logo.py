# Generated by Django 5.0.4 on 2024-04-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0004_teams_fondo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='fondo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teams',
            name='logo',
            field=models.CharField(max_length=50),
        ),
    ]
