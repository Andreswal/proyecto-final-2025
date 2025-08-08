
from django import forms
from .models import Comentario, Articulo, Categoria

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escribí tu comentario aquí...',
                'class': 'form-control'
            }),
        }
        labels = {
            'contenido': ''
        }

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'imagen_principal','imagen_intermedia', 'categoria']
