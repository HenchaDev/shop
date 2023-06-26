from django.urls import path, include
from .views import about, services, catalog, contact, shoes

urlpatterns = [
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('', catalog, name='catalog'),
    path('contact/', contact, name='contact' ),
    path('shoes/', shoes, name='shoes')
]