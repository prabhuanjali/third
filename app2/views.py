from django.shortcuts import render
from django.http import HttpResponse

def soumya(request):
    return HttpResponse('<h1><marquee>My name is soumya, and i am not a terrorist</h1></marquee>')


def Abhinash(request):
    return HttpResponse('<h1><marquee>My name is Abhinash, and i am GhodaMaggu</h1></marquee>')



# Create your views here.
