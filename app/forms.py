from django import forms
from .models import Categoria,Livro,Ajuda

class FormLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormAjuda(forms.ModelForm):
    class Meta:
        model = Ajuda
        fields = '__all__'