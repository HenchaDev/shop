from django.urls import path, include
from .views import hello, HelloView

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello-class/', HelloView.as_view(), name='hello-class'),
]