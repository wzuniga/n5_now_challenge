#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.parse
from oauth2_provider.models import AccessToken
from django.core.exceptions import ValidationError, BadRequest
from datetime import datetime


def get_oauth_access_token(request):
    """Get access token from Query string on META request and
        math with Oauth Access token class


    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    parameters = request.META['QUERY_STRING']
    parsed_parameters = urllib.parse.parse_qs(parameters)
    access_token = \
        AccessToken.objects.get(token=parsed_parameters['access_token'
                                ][0])
    return access_token


def verify_request_body(request_body, required_items):
    for item in required_items:
        if not item in request_body:
            raise ValidationError('Expected different content body!')


def verify_timestamp(timestamp_request):
    if timestamp_request > datetime.now():
        raise ValidationError('The given timestamp is invalid')


def verify_content_type(request):
    if not request.META['CONTENT_TYPE'] == 'application/json':
        return BadRequest('Method not alloed, just CONTENT_TYPE=application/json'
                          )
