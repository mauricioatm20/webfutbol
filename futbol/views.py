from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from futbol.models import Teams


class IndexView(ListView):
    template_name = "equipo_list.html"
    context_object_name = "equipo_list"
    queryset = Teams.objects.all()  # Utiliza el ORM de Django para obtener todos los equipos

def equipo_detalle(request, equipo_id):
    equipo = get_object_or_404(Teams, pk=equipo_id)
    jugadores = equipo.player_set.all()  # Recupera todos los jugadores asociados a este equipo
    return render(request, 'equipo_detalle.html', {'equipo': equipo, 'jugadores': jugadores})

