from django.urls import path
from . import views
from ticket.views import ApiTicketEndpoint

urlpatterns = [
    path('generar_informe', views.get_ticket_by_email),
    path('cargar_infraccion', ApiTicketEndpoint.as_view()),
]
