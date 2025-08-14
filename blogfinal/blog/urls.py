from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('articulo/<int:articulo_id>/toggle_like/', views.toggle_like, name='toggle_like'),
    path('articulo/nuevo/', views.crear_articulo, name='crear_articulo'),
    path('articulo/<int:articulo_id>/editar/', views.editar_articulo, name='editar_articulo'),
    path('articulo/<int:articulo_id>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
