from django.urls import path
from rest_libro.views import descripcion, lista_libros
from rest_libro.viewsLogin import login

urlpatterns = [
    path('lista_libros', lista_libros , name="lista_libros"),
    path('descripcion/<id>', descripcion, name="descripcion"),
    path('login', login, name="login"),
 
]