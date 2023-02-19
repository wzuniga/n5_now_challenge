#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, HttpResponseServerError, \
    HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseNotFound
from oauth2_provider.views.generic import ProtectedResourceView
from .models import Person, Vehicle, Officer, Ticket
from datetime import datetime
import json
from rest_framework.decorators import api_view
from django.core import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError, BadRequest
from rest_framework.parsers import JSONParser
from .utils import get_oauth_access_token, verify_request_body, \
    verify_timestamp, verify_content_type


class ApiTicketEndpoint(ProtectedResourceView):

    """Class to define API REST """

    parser_classes = [JSONParser]

    @csrf_exempt
    def post(self, request):

        """POST method to create Ticket record on data base

        Returns:
            HttpResponse: Ticket was created successfully
        """

        try:
            verify_content_type(request)
            access_token = get_oauth_access_token(request)

            request_body = json.loads(request.body)
            verify_request_body(request_body, ['placa_patente',
                                'timestamp', 'comentarios'])

            vehicle_request = \
                Vehicle.objects.get(patent_plate=request_body['placa_patente'
                                    ])
            officer_request = \
                Officer.objects.get(credential_application=access_token.application.id)

            timestamp_request = \
                datetime.fromtimestamp(request_body['timestamp'])
            verify_timestamp(timestamp_request)

            new_ticket = \
                Ticket(timestamp=timestamp_request.strftime('%Y-%m-%d %H:%M:%S.%f'
                       ), comments=request_body['comentarios'],
                       vehicle=vehicle_request,
                       officer=officer_request,
                       person=vehicle_request.person)
            new_ticket.save()
            return HttpResponse('ticket created successfully!')
        except BadRequest:

            return HttpResponseNotAllowed('Method not alloed, just CONTENT_TYPE=application/json'
                    )
        except Vehicle.DoesNotExist or Officer.DoesNotExist:
            return HttpResponseNotFound('The information given has errors, check placa_patente'
                    )
        except ValidationError or json.decoder.JSONDecodeError:
            return HttpResponseBadRequest('Content JSON body is invalid!'
                    )
        except:
            return HttpResponseServerError('Content body is invalid!')


@api_view(['GET'])
@csrf_exempt
def get_ticket_by_email(request):

    """Function to retrive all tickets from a given email

    Returns:
        HttpResponse: JSON object containing Ticket list
    """

    try:
        e_mail_request = request.GET['email']
        validate_email(e_mail_request)
        person_request = \
            Person.objects.filter(e_mail=e_mail_request).first()
        tickets_requested = Ticket.objects.filter(person=person_request)

        qs_json = serializers.serialize('json', tickets_requested,
                use_natural_foreign_keys=True,
                use_natural_primary_keys=True)

        return HttpResponse(qs_json, content_type='application/json')
    except ValidationError as e:
        return HttpResponseBadRequest('E-mail is invalid!')
