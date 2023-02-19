from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
from .models import Person, Vehicle, Officer, Ticket
from datetime import datetime
from oauth2_provider.models import AccessToken
import urllib.parse
import json
import re

class ApiTicketEndpoint(ProtectedResourceView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        app_tk = request.META["QUERY_STRING"]
        parsed = urllib.parse.parse_qs(app_tk)
        request_body = json.loads(request.body)
        acc_tk = AccessToken.objects.get(token=parsed["access_token"][0])
        vehicle_request = Vehicle.objects.get(placa_patente=request_body['placa_patente'])
        officer_request = Officer.objects.get(credential_application=acc_tk.application.id)
        person_request = vehicle_request.persona
        
        timestamp_string = request_body['timestamp']
        new_papeleta = Ticket(
            timestamp=datetime.fromtimestamp(timestamp_string).strftime('%Y-%m-%d %H:%M:%S'),
            comentarios=request_body['comentarios'],
            vehiculo=vehicle_request,
            oficial=officer_request,
            persona=person_request,
        )
        new_papeleta.save()
        return HttpResponse('Hello, OAuth2! post')


@csrf_exempt
def create_papeleta(request):
    print("enter")
    if request.method == 'POST':
        print(request)
        return HttpResponse('POST!', status=200)
    else:
        return HttpResponse('GET!', status=500)
