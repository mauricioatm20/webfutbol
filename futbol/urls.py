from django.urls import path
from .views import IndexView



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('equipos/<int:equipo_id>/', IndexView.equipo_detalle, name='equipo_detalle'),
]
