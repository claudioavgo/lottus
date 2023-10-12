from django.shortcuts import render
from django.http import HttpResponse

# Página principal
def home(request):
    return render(request, "home/home.html")