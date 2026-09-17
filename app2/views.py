from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vista1(request):
    return HttpResponse("Hola desde la vista 1 de app2")

def vista2(request):
    return HttpResponse("Hola desde la vista 2 de app2")