from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    
    ##AGREGAR
    path('agregar_profesor/', agregar_profesor, name='agregar_profesor'),
    path('agregar_alumno/', agregar_alumno, name='agregar_alumno'),
    path('agregar_curso/', agregar_curso, name='agregar_curso'),
]