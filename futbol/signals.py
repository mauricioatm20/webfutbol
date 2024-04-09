from django.db.models.signals import post_save
from django.dispatch import receiver
from futbol.models import PartidoResultado

# Esta función se ejecutará cada vez que se guarde un PartidoResultado
@receiver(post_save, sender=PartidoResultado)
def actualizar_puntos(sender, instance, created, **kwargs):
    # Verificar si se ha creado un nuevo PartidoResultado
    if created:
        # Actualizar los puntos de los equipos involucrados en el partido
        instance.equipo_local.points += calcular_puntos(instance.goles_local, instance.goles_visitante)
        instance.equipo_local.save()

        instance.equipo_visitante.points += calcular_puntos(instance.goles_visitante, instance.goles_local)
        instance.equipo_visitante.save()


# Función para calcular los puntos según los goles marcados en un partido
def calcular_puntos(goles_equipo_a, goles_equipo_b):
    if goles_equipo_a > goles_equipo_b:
        return 3
    elif goles_equipo_a == goles_equipo_b:
        return 1
    else:
        return 0