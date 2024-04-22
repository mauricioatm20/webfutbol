
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from futbol.models import Teams, puntos_equipo, Player
import matplotlib.pyplot as plt
from io import BytesIO
import base64


class IndexView(ListView):

    def acceso_home(request):
        template_name = "equipo_list.html"
        context_object_name = "equipo_list"
        queryset = Teams.objects.all()  # Utiliza el ORM de Django para obtener los datos de todos los equipos
        return render(request, template_name, {context_object_name: queryset})

    def generar_grafico(equipo_id):
        puntos_por_jornada = puntos_equipo.objects.filter(team=equipo_id).order_by('jornada')
        jornadas = []
        puntos = []
        puntos_acumulados = 0

        for resultado in puntos_por_jornada:
            jornadas.append(resultado.jornada)
            puntos_acumulados += resultado.puntos
            puntos.append(puntos_acumulados)

        # Generar el gráfico lineal
        plt.figure(figsize=(10, 6))
        plt.plot(jornadas, puntos, marker='o', linestyle='-', color='red')
        plt.xlabel('Jornada', color='white', fontsize=15)
        plt.ylabel('Puntos', color='white', fontsize=15)
        plt.title('Rendimiento del equipo por jornada',color='white', fontsize=15)
        plt.xticks(range(0, 9), color='red')
        plt.yticks(range(0, 10), color='white')

        plt.grid(True, color='white',linewidth=1)
        plt.gca().patch.set_facecolor('none')  # Establecer el fondo del gráfico como transparente
        plt.gcf().patch.set_alpha(0)

        # Guardar el gráfico en un buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        grafico_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return grafico_base64

    def equipo_detalle(request, nombre_equipo):
        equipo = get_object_or_404(Teams, team=nombre_equipo)
        jugadores = equipo.player_set.all()  # Recupera todos los jugadores asociados a este equipo

        # Obtener el ID del equipo
        equipo_id = equipo.id

        # Llamar a la función para generar el gráfico
        grafico_base64 = IndexView.generar_grafico(equipo_id)


        # Renderizar la plantilla con el gráfico
        return render(request, 'equipo_detalle.html',
                      {'equipo': equipo, 'jugadores': jugadores, 'grafico_base64': grafico_base64})

    def jugadores_list(request, equipo_id):
        # Obtener el equipo asociado a este conjunto de jugadores
        equipo = get_object_or_404(Teams, pk=equipo_id)

        # Recuperar todos los jugadores asociados a este equipo
        jugadores = equipo.objects.filter(equipo=equipo)

        # Renderizar la plantilla con la lista de jugadores
        return render(request, 'jugadores_list.html', {'equipo': equipo, 'jugadores': jugadores})


