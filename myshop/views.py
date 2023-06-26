
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
    
def catalog(request):
    return render(request, 'catalog.html')

def contact(request):
    return render(request, 'contact.html')


def shoes(request):
    return render(request, 'shoes.html')