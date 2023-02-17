from django.db import models
from django.utils import timezone

class Persona(models.Model):
    nombre = models.CharField(max_length=100)

    correo_electrónico = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.nombre


class Vehiculo(models.Model):
    placa_patente = models.CharField(max_length=6)

    marca = models.CharField(max_length=100)

    color = models.CharField(max_length=100)

    persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, )

    def __str__(self) -> str:
        return self.placa_patente


class Oficial(models.Model):
    nombre = models.CharField(max_length=100)

    numero_unico_identificacion = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nombre


class Papeleta(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)

    comentarios = models.TextField(default="")

    persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING)

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.DO_NOTHING)

    oficial = models.ForeignKey(Oficial, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.persona.nombre} - {self.vehiculo}'
