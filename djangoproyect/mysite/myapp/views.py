from django.http import HttpResponse
from .models import Usuario_Lista, Nombre_Lista
from django.shortcuts import render, get_object_or_404
# Create your views here.
def index(request):
    title = 'Django bien proooo!!'
    return render(request,'index.html',{
        'titulo' : title 
    })


def hello(request, username):
    print (username)
    return HttpResponse("<h1>Hola %s<h1/>" % username)
    

def about(request):
    username = 'codink'
    return render(request,'about.html',{
        'username': username
    })


def usuarios(request):
    #projects=list(Project.objects.values())
    usuarios = Usuario_Lista.objects.all()
    return render(request,'usuarios.html',{
        'usuarios': usuarios
    })


def listas(request):
    #task= get_object_or_404(Task, title = title)
    listas = Nombre_Lista.objects.all
    return render(request, 'listas.html',{
        'listas': listas
    })