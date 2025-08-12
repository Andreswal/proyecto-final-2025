from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

def ruta_imagen_articulo(instance, filename):
    return f'publicaciones/articulo_{instance.id}/principal{filename}'

def ruta_imagen_articulo(instance, filename):
    return f'publicaciones/articulo_{instance.id}/intermedia{filename}'

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen_principal = models.ImageField(upload_to=ruta_imagen_articulo, blank=True, null=True)
    imagen_intermedia = models.ImageField(upload_to=ruta_imagen_articulo, blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Like(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'articulo')  # Solo 1 like por usuario por artículo
    
    from django.contrib.auth.models import User

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username} - {self.articulo.titulo}"
    

        
