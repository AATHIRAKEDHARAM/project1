from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def program(request):
    return HttpResponse('hello')

def index(request):
    return render(request,'facebook.html')