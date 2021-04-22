from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, and some stuff")
# Create your views here.
