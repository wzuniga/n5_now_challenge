from django.urls import path
from . import views
from papeleta.views import ApiEndpoint

urlpatterns = [
    path('generar_informe', views.create_papeleta),
    path('cargar_infraccion', ApiEndpoint.as_view()),
]
