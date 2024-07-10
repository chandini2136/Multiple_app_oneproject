from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>Python is a programming language</h1>')

def second(request):
    return HttpResponse('<h1>Django is a python framework</h1>')
    