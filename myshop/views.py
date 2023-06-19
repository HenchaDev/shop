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

def folder_contents(request, folder_id):
    folder = Folder.objects.get(id=folder_id)
    contents = folder.contents.all()

    context = {
        'folder': folder,
        'contents': contents
    }

    return render(request, 'folder_contents.html', context)