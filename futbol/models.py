from django.db import models

class Teams(models.Model):
    team = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logos")
    total_points = models.IntegerField(default=0)  # Campo para almacenar los puntos

class Player(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)

class PartidoResultado(models.Model):
    equipo_local = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='partidos_local', verbose_name='Equipo local')
    equipo_visitante = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='partidos_visitante', verbose_name='Equipo visitante')
    goles_local = models.PositiveIntegerField(verbose_name='Goles equipo local', default=0)
    goles_visitante = models.PositiveIntegerField(verbose_name='Goles equipo visitante', default=0)


class puntos_equipo(models.Model):
    jornada = models.PositiveIntegerField(verbose_name='Jornada')
    puntos= models.PositiveIntegerField(verbose_name='Puntos')
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)