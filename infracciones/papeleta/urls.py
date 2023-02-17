from django.urls import path
from . import views

urlpatterns = [
    path('cargar_infraccion/', views.create_papeleta),
]
