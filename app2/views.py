from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def meghana(request):
    return HttpResponse('<h1>My name is meghana sir</h1>')