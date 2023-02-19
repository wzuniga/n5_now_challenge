#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from oauth2_provider.models import Application

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]{6}$',
                              'Solo 6 caracteres alphanumericos son permitidos.'
                              )
numeric = RegexValidator(r'^[0-9]{8}$',
                         'Solo 8 caracteres num\xc3\xa9ricos son permitidos.'
                         )


class Person(models.Model):

    identification_document = models.CharField(
        max_length=8,
        unique=True,
        validators=[numeric]
    )

    name = models.CharField(max_length=100)

    e_mail = models.EmailField(max_length=254, unique=True)

    def natural_key(self):
        return (self.identification_document, self.name, self.e_mail)

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    patent_plate = models.CharField(
        max_length=6,
        validators=[alphanumeric],
        unique=True
    )

    brand = models.CharField(max_length=100)

    color = models.CharField(max_length=100)

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        db_column='person_id'
    )

    def natural_key(self):
        return (self.patent_plate, self.brand, self.color)

    def __str__(self):
        return self.patent_plate


class Officer(models.Model):

    name = models.CharField(max_length=100)

    identification_number = models.CharField(
        max_length=8,
        unique=True,
        validators=[numeric]
    )

    credential_application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        db_column='credential_application_id'
    )

    def natural_key(self):
        return (self.name, self.identification_number)

    def __str__(self):
        return self.name


class Ticket(models.Model):

    timestamp = models.DateTimeField(default=timezone.now)

    comments = models.TextField(default='')

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

    def natural_key(self):
        return (self.timestamp, self.comments)

    def __str__(self):
        return f'{self.person.name} - {self.vehicle.patent_plate}'
