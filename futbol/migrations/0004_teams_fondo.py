# Generated by Django 5.0.4 on 2024-04-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0003_player_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='fondo',
            field=models.ImageField(default=0, upload_to='fondo'),
            preserve_default=False,
        ),
    ]