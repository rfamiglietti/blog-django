# posts/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Boas-vindas ao Blog!</h1>")