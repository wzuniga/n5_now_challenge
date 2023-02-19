from django.contrib import admin
from .models import Person, Vehicle, Officer, Ticket

admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Officer)


@admin.register(Ticket)
class PostPepeleta(admin.ModelAdmin):
    list_display = []