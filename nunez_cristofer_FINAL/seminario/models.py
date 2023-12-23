# seminario/models.py
from django.db import models

class Institucion(models.Model):
    nombre_institucion = models.CharField(max_length=100, null=True, blank=True)
    telefono_institucion = models.CharField(max_length=20, null=True, blank=True)
    direccion_institucion = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.nombre_institucion

class Inscrito(models.Model):
    ESTADOS = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    )

    nombre_persona = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre_persona
