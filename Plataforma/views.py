from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View
from django.shortcuts import redirect

########################
#-----VIEW HOME
########################

def home(request):
    return render(request, 'plataforma/home.html')


########################
#-----VIEW AGREGAR PROFESOR
########################

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm()
        
    return render(request, 'plataforma/agregar_profesor.html', {'form': form})


########################
#-----VIEW AGREGAR ALUMNO
########################

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
        
    return render(request, 'plataforma/agregar_alumno.html', {'form': form})


########################
#-----VIEW AGREGAR CURSO
########################

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'plataforma/agregar_curso.html', {'form': form})


########################
#-----VIEW LISTAR PROFESORES
########################

def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'plataforma/listar_profesores.html', {'profesores': profesores})


########################
#-----VIEW LISTAR PROFESORES
########################

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'plataforma/listar_alumnos.html', {'alumnos': alumnos})

########################
#-----VIEW LISTAR CURSOS
########################
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'plataforma/listar_cursos.html', {'cursos': cursos})
    
