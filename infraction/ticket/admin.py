#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin


class PostPerson(admin.ModelAdmin):

    list_display = ['name', 'identification_document', 'e_mail']


class PostVehicle(admin.ModelAdmin):

    list_display = ['patent_plate', 'brand', 'color', 'person']


class PostOfficer(admin.ModelAdmin):

    list_display = ['name', 'identification_number',
                    'credential_application']


class PostTicket(admin.ModelAdmin):

    list_display = ['person', 'vehicle', 'officer', 'timestamp']
