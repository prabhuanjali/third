from django.shortcuts import render
from django.http import HttpResponse

def anjali(request):
    return HttpResponse('<h1><marquee>This is my first App1 Response</h1></marquee>')

def satabdi(request):
    return HttpResponse('<h1><marquee>This is my second app1 response</h1></marquee>')



# Create your views here.
