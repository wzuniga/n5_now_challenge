from django.contrib import admin
from .models import Persona, Vehiculo, Oficial, Papeleta

admin.site.register(Persona)
admin.site.register(Vehiculo)
admin.site.register(Oficial)


@admin.register(Papeleta)
class PostPepeleta(admin.ModelAdmin):
    list_display = []