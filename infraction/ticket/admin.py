#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Person, Vehicle, Officer, Ticket


@admin.register(Person)
class PostPerson(admin.ModelAdmin):

    """Class to customize the items in the Person model for the
        administration panel"""

    list_display = ['name', 'identification_document', 'e_mail']


@admin.register(Vehicle)
class PostVehicle(admin.ModelAdmin):

    """Class to customize the items in the Vehicle model for the
        administration panel"""

    list_display = ['patent_plate', 'brand', 'color', 'person']


@admin.register(Officer)
class PostOfficer(admin.ModelAdmin):

    """Class to customize the items in the Officer model for the
        administration panel"""

    list_display = ['name', 'identification_number',
                    'credential_application']


@admin.register(Ticket)
class PostTicket(admin.ModelAdmin):

    """Class to customize the items in the Ticket model for the
        administration panel"""

    list_display = ['person', 'vehicle', 'officer', 'timestamp']
