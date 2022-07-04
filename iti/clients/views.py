from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def clientsIndex(request):
    # static content 
    return HttpResponse("This is all clients page ")


def home(request):
    return render(request, "clients/homepage.html")
