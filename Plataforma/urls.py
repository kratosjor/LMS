from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    
    ##AGREGAR
    path('agregar_profesor/', agregar_profesor, name='agregar_profesor'),
    path('agregar_alumno/', agregar_alumno, name='agregar_alumno'),
    path('agregar_curso/', agregar_curso, name='agregar_curso'),
    
    ##LISTAR
    path('listar_profesores/', listar_profesores, name='listar_profesores'),
    path('listar_alumnos/', listar_alumnos, name='listar_alumnos'),
    path('listar_cursos/', listar_cursos, name='listar_cursos'),
]