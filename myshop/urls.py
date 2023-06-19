from django.urls import path, include
from .views import about, services, catalog, contact, folder_contents

urlpatterns = [
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('', catalog, name='catalog'),
    path('contact/', contact, name='contact' ),
    path('folder/<int:folder_id>/', folder_contents, name='folder_contents'),
]