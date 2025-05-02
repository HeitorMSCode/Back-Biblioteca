from django.contrib import admin
from .models import Categoria,Livro,Ajuda

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Livro)
admin.site.register(Ajuda)