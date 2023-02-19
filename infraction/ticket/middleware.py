#!/usr/bin/python
# -*- coding: utf-8 -*-


class CustomMiddleware:

    """Class to customize middleware for oauth application"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
