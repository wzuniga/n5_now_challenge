#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.parse
from oauth2_provider.models import AccessToken
from django.core.exceptions import ValidationError, BadRequest
from datetime import datetime


def get_oauth_access_token(request):
    """Get access token from Query string on META request and
        match with Oauth Access token class


    Args:
        request: request object from ProtectedResourceView 

    Returns:
        access_token: Token store on data base for AccessToken model
    """

    parameters = request.META['QUERY_STRING']
    parsed_parameters = urllib.parse.parse_qs(parameters)
    access_token = \
        AccessToken.objects.get(token=parsed_parameters['access_token'
                                ][0])
    return access_token


def verify_request_body(request_body, required_items):

    """Validate that the whole list is in request_body key list

    Args:
        request_body: request object from json.loads() function 
        required_items: List with strings the are required

    Raises:
        ValidationError: raise when one item from a list is missing
    """

    for item in required_items:
        if not item in request_body:
            raise ValidationError('Expected different content body!')


def verify_timestamp(timestamp_request):

    """Valdiate that timestamp given is before than current datetime

    Args:
        timestamp_request: timestamp to be validated

    Raises:
        ValidationError: raise when timestamp given is
            latter than current datetime
    """

    if timestamp_request > datetime.now():
        raise ValidationError('The given timestamp is invalid')


def verify_content_type(request):

    """Validate that CONTENT_TYPE is equal to application/json

    Args:
        request: request object from ProtectedResourceView 

    Returns:
        BadRequest: returns when CONTENT_TYPE is different to application/json
    """

    if not request.META['CONTENT_TYPE'] == 'application/json':
        return BadRequest('Method not alloed, just CONTENT_TYPE=application/json'
                          )
