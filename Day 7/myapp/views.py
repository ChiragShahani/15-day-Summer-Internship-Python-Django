from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse('<h1> Welcome to Django </h1>')

def aboutpageview(request):
    return HttpResponse('About us')

def contactpageview(request):
    return HttpResponse('Contact us')