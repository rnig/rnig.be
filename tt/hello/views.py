from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def howdie(request, name):
    return render(request, "hello/howdie.html", {
        "name": name.capitalize()
    })

def say(request):
    return HttpResponse("Hello?")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

