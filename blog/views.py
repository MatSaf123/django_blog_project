from django.shortcuts import render
from django.http import HttpResponse


def home(request):  # this function handles traffic from homepage
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
