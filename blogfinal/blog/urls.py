from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:categoria_id>/', views.articulos_por_categoria, name='articulos_por_categoria'),
    path('articulo/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('comentario/<int:comentario_id>/editar/', views.editar_comentario, name='editar_comentario'),
    path('comentario/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('categoria/<int:categoria_id>/', views.articulos_por_categoria, name='articulos_por_categoria'),

]
