from django.shortcuts import render

def inicio(request):
    return render(request,'inicio.html')

def livros(request):
    return render(request,'livros.html')

def cadLivros(request):
    return render(request,'cad-livros.html')

def editLivros(request):
    return render(request, 'edit-livros.html')

def cadCategoria(request):
    return render(request, 'cad-categoria.html')

def categoria(request):
    return render(request,'categorias.html')

def viewCategoria(request):
    return render(request,'view-categoria.html')

def viewLivro(request):
    return render(request,'view-livros.html')