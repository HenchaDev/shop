from django.urls import path, include
from .views import about, HelloView, catalog, contact

urlpatterns = [
    path('about/', about, name='about'),
    path('hello-class/', HelloView.as_view(), name='hello-class'),
    path('', catalog, name='catalog'),
    path('contact/', contact, name='contact' ),
]