# Register your models here.
from django.contrib import admin

from .models import Teams, Player, PartidoResultado, puntos_equipo

admin.site.register(Teams)
admin.site.register(Player)
admin.site.register(PartidoResultado)
admin.site.register(puntos_equipo)