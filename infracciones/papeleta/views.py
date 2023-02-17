from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_papeleta(request):
    print("enter")
    if request.method == 'POST':
        print(request)
        print("enter")
