from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request.META)
    return HttpResponse(request.META['REMOTE_ADDR'])


# Create your views here.
