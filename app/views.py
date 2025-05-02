from django.shortcuts import render, redirect
from .models import Categoria, Livro, Ajuda
from .forms import FormLivro, FormCategoria, FormAjuda

def inicio(request):
    return render(request,'inicio.html')

def livros(request):

    todos_livros = Livro.objects.all()

    contexto = {
        "livros" : todos_livros
    }

    return render(request,'livros.html',contexto)

def cadLivros(request):

    if request.method == 'POST':
        form = FormLivro(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("url_livros")
    else:
        form = FormLivro()

    contexto = {
        "formulario":form
    }

    return render(request,'cad-livros.html',contexto)

def editLivros(request):
    return render(request, 'edit-livros.html')

def cadCategoria(request):
   
    if request.method == 'POST':
        form = FormCategoria(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("url_categoria")
    else:
        form = FormCategoria()

    contexto = {
        "formulario":form
    } 

    return render(request, 'cad-categoria.html', contexto)

def ajuda(request):
    
    if request.method == 'POST':
        form = FormAjuda(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormAjuda()

    contexto = {
        "formulario":form
    }

    return render(request,'ajuda.html', contexto)

def buscarLivroPorCategoria(request,pk):
    buscar = Livro.objects.filter(categoria = pk)
    categoria = Categoria.objects.get(pk = pk)

    contexto = {
        "buscar_por_livros": buscar,
        "categoria": categoria
    }

    return render(request, 'view-categoria.html', contexto)

def categoria(request):
    todas_categorias = Categoria.objects.all()

    contexto = {
        "categorias_adicionadas": todas_categorias
    }

    return render(request,'categorias.html', contexto)

def viewLivro(request,pk):
    livro = Livro.objects.get(pk = pk)

    contexto = {
        'livro_encontrado': livro
    }

    return render(request,'view-livros.html', contexto)

def viewAjuda(request):
    ajuda = Ajuda.objects.all()

    contexto = {
        "vizualizar_ajudas": ajuda
    }

    return render(request,'view-ajudas.html', contexto)
