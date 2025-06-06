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
    
    #DETALLE
    path('detalle_curso/<int:curso_id>/', detalle_curso, name='detalle_curso'),
    path('cursos/<int:curso_id>/agregar-material/', agregar_material, name='agregar_material'),
    path('cursos/<int:curso_id>/materiales/', ver_materiales, name='ver_materiales'),
    path('material/<int:material_id>/', detalle_material, name='detalle_material'),
    path('material/<int:pk>/editar/', MaterialUpdateView.as_view(), name='editar_material'),

    #EDICION
    path('editar_curso/<int:pk>/', CursoUpdateView.as_view(), name='editar_curso'),
    path('editar_alumno/<int:pk>/', AlumnoUpdateView.as_view(), name='editar_alumno'),
    
    #ACTIVIDAD
    path('cursos/<int:curso_id>/crear_actividad/', crear_actividad, name='crear_actividad'),
    path('curso/<int:curso_id>/actividades/', ver_actividad, name='ver_actividad'),
    path('actividad/<int:actividad_id>/realizar/', realizar_actividad, name='realizar_actividad'),
    path('actividad/<int:actividad_id>/resultado/', resultado_actividad, name='resultado_actividad'),


    path('actividad/<int:pk>/eliminar_actividad/', ActividadDeleteView.as_view(), name='eliminar_actividad'),



]