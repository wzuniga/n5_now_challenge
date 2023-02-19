from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
from .models import Papeleta, Vehiculo, Oficial, Persona
from datetime import datetime
from oauth2_provider.models import AccessToken
import urllib.parse
import json
import re

class ApiEndpoint(ProtectedResourceView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        print("#######_")
        print(request.META["QUERY_STRING"])
        print(request.META["HTTP_HOST"])
        app_tk = request.META["QUERY_STRING"]
        parsed = urllib.parse.parse_qs(app_tk)
        request_body = json.loads(request.body)
        print(parsed)
        print(parsed["access_token"])
        print(parsed["access_token"][0])
        #app_tk = m.group(3)
        acc_tk = AccessToken.objects.get(token=parsed["access_token"][0])
        #user = acc_tk.user
        print("#######_2")
        print(acc_tk.user)
        print("#######_3")
        print(acc_tk.application.client_id)
        print(acc_tk.application.id)
        vehicle_request = Vehiculo.objects.get(placa_patente=request_body['placa_patente'])
        officer_request = Oficial.objects.get(credential_application=acc_tk.application.id)
        person_request = vehicle_request.persona
        print(vehicle_request)
        print(officer_request)
        print(person_request)
        print("#######")
        valid, r = self.verify_request(request)
        print("r.user ", r.user)
        print("request.user ", request.user)
        print("request.resource_owner ", request.resource_owner)
        print("args ", args)
        print("kwargs ", kwargs)
        #print("The dir() method returns: ", dir(request))
        print("#######")
    
        
        print(request_body)

        print("--------")
        print(Vehiculo.objects.get(placa_patente=request_body['placa_patente']))
        print("--------")
        
        timestamp_string = request_body['timestamp']
        new_papeleta = Papeleta(
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

