from django.db import models

# Create your models here.

#modelo para la la categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria


class Libro(models.Model):
    isbn = models.CharField(max_length=6, primary_key=True, verbose_name='ISBN')
    nombre= models.CharField(max_length=20, verbose_name='Nombre')
    autor = models.CharField(max_length=20, null=True, blank=True, verbose_name='Autor')
    descripcion = models.CharField(max_length=100, null=True, blank=True , verbose_name='descripcion')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.isbn