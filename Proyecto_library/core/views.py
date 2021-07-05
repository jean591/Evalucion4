
from django.shortcuts import render,redirect
from .models import Libro
from .forms import LibroForm

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def login(request):
    return render(request,'core/login.html')

def signUp(request):
    return render(request,'core/signUp.html')

def registro(request):
    libros = Libro.objects.all()
    datos = {
        'libros': libros
    }
    return render(request, 'core/registro.html', datos)


def form_libro(request):
    datos = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_libro.html', datos)


def form_mod_libro(request, id):
    libro = Libro.objects.get(isbn=id)
    datos = {
        'form': LibroForm(instance=libro)
    }
    if request.method == 'POST':
        formulario =  LibroForm(data=request.POST, instance=libro)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_libro.html', datos)




def form_del_libro(request, id):
    libro = Libro.objects.get(isbn=id)
    libro.delete()
    return redirect(to="registro")

