from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<H1>Hello everybody! This is my first Django app.</H1>")