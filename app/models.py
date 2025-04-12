from django.db import models

class Categoria(models.Model):
    nome = models.CharField(verbose_name="Nome da categoria", max_length=50)
    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome_do_livro = models.CharField(verbose_name="Nome do livro", max_length=200)
    nome_do_autor = models.CharField(verbose_name="Nome do autor", max_length=350)
    data_lancamento = models.DateField(verbose_name="Data de lançamento")
    capa_do_livro = models.ImageField(upload_to="livros", verbose_name="Capa do livro")
    categoria = models.ManyToManyField(Categoria)
    estante_do_livro = models.IntegerField(verbose_name="Numeração da estante")

# nome do livro
# nome do autor
# data de lançamento
# capa do livro
# categoria do livro
# estante livro