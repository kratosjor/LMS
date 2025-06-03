from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, DetailView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
import json
from django.http import QueryDict
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


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
    buscar_profesor = request.GET.get('profesor', '')

    if buscar_profesor:
        profesores = Profesor.objects.filter(
            Q(nombre__icontains=buscar_profesor) |
            Q(apellidos__icontains=buscar_profesor)
        )
    else:
        profesores = Profesor.objects.all()

    return render(request, 'plataforma/listar_profesores.html', {
    'profesores': profesores,
    'buscar_profesor': buscar_profesor
})



########################
#-----VIEW LISTAR alumnos
########################

def listar_alumnos(request):
    buscar_alumno = request.GET.get("alumno", "")
    if buscar_alumno:
        alumnos = Alumno.objects.filter(
            Q(nombre__icontains=buscar_alumno) |
            Q(apellidos__icontains=buscar_alumno) 
        )
    
    else:
        alumnos = Alumno.objects.all()
    
    
    return render(request, 'plataforma/listar_alumnos.html', {'alumnos': alumnos,'buscar_alumno':buscar_alumno})

########################
#-----VIEW LISTAR CURSOS
########################
def listar_cursos(request):
    buscar_curso = request.GET.get("curso", "")
    
    if buscar_curso:
        cursos = Curso.objects.filter(nombre_curso__icontains=buscar_curso)
    else:
        cursos = Curso.objects.all()
    
    return render(request, 'plataforma/listar_cursos.html', {
        'cursos': cursos,
        'buscar_curso': buscar_curso
    })


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
    

##########################
#-----VIEW EDITAR CURSO
##########################  

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = 'plataforma/editar_curso.html'
    fields = ['nombre_curso', 'profesor_curso', 'fecha_inicio', 'fecha_fin', 'modalidad', 'descripcion']
    
    def get_success_url(self):
        return reverse_lazy('detalle_curso', kwargs={'curso_id': self.object.id})


##########################
#-----VIEW EDITAR ALUMNO
##########################  

class AlumnoUpdateView(UpdateView):
    model = Alumno
    template_name = 'plataforma/editar_alumno.html'
    fields = ['nombre', 'apellidos', 'email', 'telefono', 'fecha_nacimiento', 'fecha_inscripcion','cursos']
    
    def get_success_url(self):
        return reverse_lazy('listar_alumnos')
    
########################
#-----VISTA CREAR ACTIVIDAD
########################
@csrf_exempt
def crear_actividad(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        actividad_form = ActividadForm(request.POST)
        if actividad_form.is_valid():
            actividad = actividad_form.save(commit=False)
            actividad.curso = curso
            actividad.save()

            # Ahora vamos a leer las preguntas y opciones desde los datos POST
            preguntas_data = json.loads(request.POST.get('preguntas_json', '[]'))

            for pregunta_data in preguntas_data:
                pregunta = Pregunta.objects.create(
                    actividad=actividad,
                    texto=pregunta_data['texto']
                )

                for opcion_data in pregunta_data['opciones']:
                    Opcion.objects.create(
                        pregunta=pregunta,
                        texto=opcion_data['texto'],
                        es_correcta=opcion_data['es_correcta']
                    )

            return redirect('detalle_curso', curso.id)
    else:
        actividad_form = ActividadForm()

    return render(request, 'plataforma/crear_actividad.html', {
        'actividad_form': actividad_form,
        'curso': curso,
    })
    
########################
#-----VISTA ver ACTIVIDADes
########################
def ver_actividad(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    actividades = Actividad.objects.filter(curso=curso)

    return render(request, 'plataforma/ver_actividad.html', {
        'curso': curso,
        'actividades': actividades,
    })
########################
#-----VISTA ELIMINAR ACTIVIDAD
########################

class ActividadDeleteView(DeleteView):
    model = Actividad
    template_name = 'plataforma/eliminar_actividad.html'

    def get_success_url(self):
        return reverse_lazy('detalle_curso', kwargs={'curso_id': self.object.curso.id})
    
########################
#-----VISTA COMPLETAR ACTIVIDAD
########################
def realizar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    preguntas = Pregunta.objects.filter(actividad=actividad).prefetch_related('opciones')

    if request.method == 'POST':
        puntaje = 0
        total = preguntas.count()
        respuestas = {}

        for pregunta in preguntas:
            seleccion = request.POST.get(f'pregunta_{pregunta.id}')
            respuestas[pregunta.id] = seleccion
            if seleccion:
                opcion = Opcion.objects.filter(id=seleccion, pregunta=pregunta).first()
                if opcion and opcion.es_correcta:
                    puntaje += 1

        return render(request, 'plataforma/resultado_actividad.html', {
            'actividad': actividad,
            'puntaje': puntaje,
            'total': total,
        })

    return render(request, 'plataforma/realizar_actividad.html', {
        'actividad': actividad,
        'preguntas': preguntas,
    })

########################
#-----VISTA RESULTADO ACTIVIDAD
########################      

def resultado_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    
    # Ejemplo ficticio: aquí deberías obtener el resultado desde la sesión o la base de datos.
    puntaje = request.session.get('puntaje', None)
    total = request.session.get('total', None)

    if puntaje is None or total is None:
        return redirect('realizar_actividad', actividad_id=actividad.id)

    return render(request, 'plataforma/resultado_actividad.html', {
        'actividad': actividad,
        'puntaje': puntaje,
        'total': total,
    })
