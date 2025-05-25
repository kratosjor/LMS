from .models import *
from django import forms


########################
#-----FORM PROFESOR
########################

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellidos', 'email', 'telefono', 'fecha_nacimiento', 'especialidad']
        widgets = {
            
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


########################
#-----FORM ALUMNO
########################

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellidos', 'email', 'telefono', 'fecha_nacimiento', 'fecha_inscripcion','cursos']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_inscripcion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cursos': forms.CheckboxSelectMultiple()  # puedes cambiar esto por un select múltiple si prefieres
        }


########################
#-----FORM CURSO
########################

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre_curso', 'profesor_curso', 'fecha_inicio', 'fecha_fin', 'modalidad', 'descripcion']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
        