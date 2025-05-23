from django.db import models

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
    alumnos_curso = models.ManyToManyField(Alumno, related_name='cursos')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    modalidad = models.CharField(max_length=100, choices=MODALIDAD_CHOICES)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre_curso} ({self.modalidad})"
