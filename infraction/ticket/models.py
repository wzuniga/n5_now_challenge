from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from users.models import User
#from django.contrib.auth.models import Application
from oauth2_provider.models import Application, AbstractApplication

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Solo caracteres alphanumericos son permitidos.')


class Person(models.Model):
    identification_document = models.CharField(max_length=8)

    name = models.CharField(max_length=100)

    e_mail = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.nombre


class Vehicle(models.Model):
    patent_plate = models.CharField(
        max_length=6,
        validators=[alphanumeric]
    )

    brand = models.CharField(max_length=100)

    color = models.CharField(max_length=100)

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        db_column='person_id'
    )

    def __str__(self) -> str:
        return self.patent_plate


class Officer(models.Model):
    name = models.CharField(max_length=100)

    identification_number = models.CharField(max_length=8)

    credential_application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        db_column='credential_application_id'
    )

    def __str__(self) -> str:
        return self.name


class Ticket(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)

    comments = models.TextField(default="")

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        db_column='person_id'
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        db_column='vehicle_id'
    )

    officer = models.ForeignKey(
        Officer,
        on_delete=models.CASCADE,
        db_column='officer_id'
    )

    def __str__(self) -> str:
        #return f'{self.persona.nombre} - {self.vehiculo.placa_patente}'
        return self.comentarios