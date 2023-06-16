from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def about(request):
    return render(request, 'about.html')

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, Class shopper!")
    
def catalog(request):
    return render(request, 'catalog.html')

def contact(request):
    return render(request, 'contact.html')