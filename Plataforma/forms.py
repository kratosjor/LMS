from .models import *
from django import forms
from django.forms import inlineformset_factory


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
        

########################
#-----FORM MATERIAL
########################

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['curso', 'titulo', 'contenido_html']
        

####################################################################################################

########################
#-----FORM  ACTIVIDAD
########################
       
class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['titulo', 'descripcion']

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['texto']

class OpcionForm(forms.ModelForm):
    class Meta:
        model = Opcion
        fields = ['texto', 'es_correcta']

# Formset para preguntas de la actividad
PreguntaFormSet = inlineformset_factory(
    Actividad, Pregunta, form=PreguntaForm, extra=1, can_delete=True
)

# Formset para opciones de cada pregunta
OpcionFormSet = inlineformset_factory(
    Pregunta, Opcion, form=OpcionForm, extra=3, can_delete=True, max_num=3, validate_max=True
)