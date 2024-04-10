import numpy as np
from django.shortcuts import get_object_or_404, render
from django.db import connection
from django.views.generic import ListView
from django.db.models import F, Sum, Subquery, OuterRef
from futbol.models import Teams, puntos_equipo
import matplotlib.pyplot as plt
from io import BytesIO
import base64

class IndexView(ListView):
    template_name = "equipo_list.html"
    context_object_name = "equipo_list"
    queryset = Teams.objects.all()  # Utiliza el ORM de Django para obtener los datos de todos los equipos

    def equipo_detalle(request, equipo_id):
        equipo = get_object_or_404(Teams, pk=equipo_id)
        jugadores = equipo.player_set.all()  # Recupera todos los jugadores asociados a este equipo

        # Obtener los puntos por jornada del equipo específico
        puntos_por_jornada = puntos_equipo.objects.filter(team=equipo_id).order_by('jornada')

        jornadas = []
        puntos = []
        puntos_acumulados = 0  # Inicializar los puntos acumulados

        for resultado in puntos_por_jornada:
            jornadas.append(resultado.jornada)
            puntos_acumulados += resultado.puntos  # Sumar los puntos de esta jornada a los puntos acumulados
            puntos.append(puntos_acumulados)  # Agregar los puntos acumulados a la lista de puntos

        # Generar el gráfico lineal
        plt.figure(figsize=(10, 6))
        plt.plot(jornadas, puntos, marker='o', linestyle='-')
        plt.xlabel('Jornada')
        plt.ylabel('Puntos')
        plt.title('Rendimiento del equipo {} por jornada'.format(equipo.team))
        plt.xticks(range(0, 9))  # Asegúrate de que las jornadas vayan de 1 a 8
        plt.yticks(range(0, 24))
        plt.grid(True)
        # Convertir el gráfico a una imagen base64
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        grafico_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        # Renderizar la plantilla con el gráfico
        return render(request, 'equipo_detalle.html',
                      {'equipo': equipo, 'jugadores': jugadores, 'grafico_base64': grafico_base64})







