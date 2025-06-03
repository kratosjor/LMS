from django.db import models
from ckeditor.fields import RichTextField  # Asegúrate de instalar django-ckeditor

########################
#-----MODELO PROFESOR
########################
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"Profesor {self.nombre} {self.apellidos}"


########################
#-----MODELO ALUMNO
########################
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    fecha_inscripcion = models.DateField()
    cursos = models.ManyToManyField('Curso', related_name='alumnos', blank=True)

    def __str__(self):
        return f"Alumno {self.nombre} {self.apellidos}"


########################
#-----MODELO CURSO
########################
class Curso(models.Model):
    MODALIDAD_CHOICES = [
        ('Mañana', 'Mañana'),
        ('Noche', 'Noche'),
        ('Fin de Semana', 'Fin de Semana'),
    ]

    nombre_curso = models.CharField(max_length=100)
    profesor_curso = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')
    max_alumnos = models.PositiveIntegerField(default=40)  # límite
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    modalidad = models.CharField(max_length=100, choices=MODALIDAD_CHOICES)
    descripcion = models.TextField()
    
    def alumnos_count(self):
        return self.alumnos.count()

    def __str__(self):
        return f"{self.nombre_curso} ({self.modalidad})"
    
########################
#-----MODELO MATERIAL
########################

class Material(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='materiales')
    titulo = models.CharField(max_length=200)
    contenido_html = RichTextField()  # Usando RichTextField para contenido enriquecido
    creado_en = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
#############################################################################################################


########################
#-----MODELO ACTIVIDAD  
########################
class Actividad(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='actividades')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
########################
#-----MODELO Pregunta
########################

class Pregunta(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='preguntas')
    texto = models.TextField()

    def __str__(self):
        return self.texto
    
########################
#-----MODELO OPCION
########################

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto