# cursos/models.py
from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='')
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.matricula} - {self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    # Relación 1:N corregida (on_delete)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')
    # Relación N:M
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos', blank=True)


    def __str__(self):
        return self.nombre
