from django.urls import path
from .views import IndexView, equipo_detalle



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('equipos/<int:equipo_id>/', equipo_detalle, name='equipo_detalle'),
]
