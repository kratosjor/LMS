from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, DetailView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy

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


########################
#-----VIEW DETALLE CURSO
########################

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id = curso_id)
    alumnos_inscritos = curso.alumnos.all()
    return render(request, 'plataforma/detalle_curso.html', {'curso': curso, 'alumnos_inscritos': alumnos_inscritos})

#########################
#-----VIEW AGREGAR MATERIAL
#########################

def agregar_material(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)  # Si manejas archivos
        if form.is_valid():
            material = form.save(commit=False)
            material.curso = curso
            material.save()
            return redirect('detalle_curso', curso_id=curso.id)  # Redirige al detalle del curso
    else:
        form = MaterialForm()
    return render(request, 'plataforma/agregar_material.html', {'form': form, 'curso': curso})

#########################
#-----VIEW VER MATERIALES
#########################

def ver_materiales(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    materiales = curso.materiales.all().order_by('id')  # Usa 'materiales' porque es el related_name
    return render(request, 'plataforma/ver_materiales.html', {
        'curso': curso,
        'materiales': materiales
    })
    
##########################
#-----VIEW DETALLE MATERIAL
##########################  

def detalle_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    return render(request, 'plataforma/detalle_material.html', {'material': material})


##########################
#-----VIEW DETALLE MATERIAL
##########################  

class MaterialUpdateView(UpdateView):
    model = Material
    template_name = 'plataforma/editar_material.html'
    fields = ['titulo', 'contenido_html']
    def get_success_url(self):
        return reverse_lazy('ver_materiales', kwargs={'curso_id': self.object.curso.id})
    
    
    
