from django.urls import path
from .views import inicio, livros, cadLivros, editLivros, cadCategoria, categoria, viewCategoria, viewLivro

urlpatterns = [
    path('',inicio, name="url_inicio"),
    path('livros/',livros, name="url_livros"),
    path('cadastrar_livro/',cadLivros, name="url_cadastrar"),
    path('editar_livro/',editLivros, name="url_editar"),
    path('cadastrar_categoria/',cadCategoria, name="url_cadCategoria"),
    path('categorias/',categoria, name="url_categoria"),
    path('visualizar_categoria',viewCategoria, name="url_viewCategoria"),
    path('visualizar_livro',viewLivro, name="url_viewLivro"),
]