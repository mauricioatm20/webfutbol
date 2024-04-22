from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView.acceso_home, name='index'),
    path('equipos/<str:nombre_equipo>/',IndexView.equipo_detalle, name='equipo_detalle'),
    path('equipos/<int:equipo_id>/jugadores/', IndexView.jugadores_list, name='jugadores_list'),
]
