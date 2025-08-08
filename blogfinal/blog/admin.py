from django.contrib import admin
from .models import Categoria, Articulo

admin.site.register(Categoria)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'autor')
fields = ('titulo', 'contenido', 'imagen_principal', 'imagen_intermedia', 'autor')