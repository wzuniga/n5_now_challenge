#!/usr/bin/python
# -*- coding: utf-8 -*-


class CustomMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.user)

        response = self.get_response(request)
        return response
