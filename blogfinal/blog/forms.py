
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

        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Título del artículo',
                'class': 'form-control'
            }),
            'contenido': forms.Textarea(attrs={
                'rows': 10,
                'placeholder': 'Escribí el contenido del artículo aquí...',
                'class': 'form-control'
            }),
            'imagen_principal': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'imagen_intermedia': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
