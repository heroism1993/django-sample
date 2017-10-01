from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request.path)
    print(request.path_info)
    return HttpResponse("Hello World.")


# Create your views here.
