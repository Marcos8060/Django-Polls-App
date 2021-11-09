from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Marcos this is your first polls index')
