from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<a href="/rango/about">About</a><br>Rango says hey the world!')

def about(request):
    return HttpResponse('<a href="/rango/">Main</a><br>Rango says here is the about page.')
