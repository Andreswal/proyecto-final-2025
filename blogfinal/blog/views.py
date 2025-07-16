from django.shortcuts import render
from .models import Articulo

def inicio(request):
    orden = request.GET.get('orden', 'fecha_desc')

    if orden == 'fecha_asc':
        articulos = Articulo.objects.all().order_by('fecha_publicacion')
    elif orden == 'titulo_asc':
        articulos = Articulo.objects.all().order_by('titulo')
    elif orden == 'titulo_desc':
        articulos = Articulo.objects.all().order_by('-titulo')
    else:
        articulos = Articulo.objects.all().order_by('-fecha_publicacion')  # Por defecto: más recientes primero

    return render(request, 'blog/inicio.html', {'articulos': articulos})


from .models import Categoria

# Vista que muestra todas las categorías
def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'blog/categorias.html', {'categorias': categorias})

# Vista que muestra artículos de una categoría específica
def articulos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    articulos = Articulo.objects.filter(categoria=categoria).order_by('-fecha_publicacion')
    return render(request, 'blog/articulos_por_categoria.html', {
        'categoria': categoria,
        'articulos': articulos
    })
def detalle_articulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    return render(request, 'blog/detalle_articulo.html', {'articulo': articulo})

def acerca_de(request):
    return render(request, 'blog/acerca_de.html')

from django.contrib import messages

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        messages.success(request, "¡Gracias por tu mensaje!")
        # Podrías guardar esto en la base de datos o enviarlo por email más adelante
    return render(request, 'blog/contacto.html')

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'blog/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

from django.http import HttpResponseForbidden

def editar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    if request.user != comentario.autor:
        return HttpResponseForbidden("No tenés permiso para editar este comentario.")
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('detalle_articulo', articulo_id=comentario.articulo.id)
    else:
        form = ComentarioForm(instance=comentario)
    
    return render(request, 'blog/editar_comentario.html', {'form': form, 'comentario': comentario})

def eliminar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    if request.user != comentario.autor:
        return HttpResponseForbidden("No tenés permiso para eliminar este comentario.")
    
    if request.method == 'POST':
        articulo_id = comentario.articulo.id
        comentario.delete()
        return redirect('detalle_articulo', articulo_id=articulo_id)
    
    return render(request, 'blog/eliminar_comentario.html', {'comentario': comentario})

def articulos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    articulos = Articulo.objects.filter(categoria=categoria).order_by('-fecha_publicacion')
    return render(request, 'blog/articulos_por_categoria.html', {
        'categoria': categoria,
        'articulos': articulos
    })
