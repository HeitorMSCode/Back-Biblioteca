from django.urls import path
from .views import inicio, livros, cadLivros, editLivros, cadCategoria, categoria, buscarLivroPorCategoria, viewLivro, ajuda, viewAjuda

urlpatterns = [
    path('',inicio, name="url_inicio"),
    path('livros/',livros, name="url_livros"),
    path('cadastrar_livro/',cadLivros, name="url_cadastrar"),
    path('editar_livro/',editLivros, name="url_editar"),
    path('cadastrar_categoria/',cadCategoria, name="url_cadCategoria"),
    path('categorias/',categoria, name="url_categoria"),
    path('visualizar_categoria/<int:pk>',buscarLivroPorCategoria, name="url_viewCategoria"),
    path('visualizar_livro/<int:pk>',viewLivro, name="url_viewLivro"),
    path('registrar_ajuda/',ajuda, name="url_ajuda"),
    path('vizualizar_ajudas/',viewAjuda, name="url_viewAjuda")
]

