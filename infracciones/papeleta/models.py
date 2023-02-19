from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from users.models import User
#from django.contrib.auth.models import Application
from oauth2_provider.models import Application, AbstractApplication

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Solo caracteres alphanumericos son permitidos.')


class Persona(models.Model):
    documento_identificacion = models.CharField(max_length=8)

    nombre = models.CharField(max_length=100)

    correo_electrónico = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.nombre


class Vehiculo(models.Model):
    placa_patente = models.CharField(max_length=6, validators=[alphanumeric])

    marca = models.CharField(max_length=100)

    color = models.CharField(max_length=100)

    persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, )

    def __str__(self) -> str:
        return self.placa_patente


class Oficial(models.Model):
    nombre = models.CharField(max_length=100)

    numero_unico_identificacion = models.CharField(max_length=8)

    credential_application = models.ForeignKey(Application, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nombre


class Papeleta(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)

    comentarios = models.TextField(default="")

    persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING)

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.DO_NOTHING)

    oficial = models.ForeignKey(Oficial, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        #return f'{self.persona.nombre} - {self.vehiculo.placa_patente}'
        return self.comentarios
