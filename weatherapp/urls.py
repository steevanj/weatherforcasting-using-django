from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('weatherdetail.urls')),
    path('home/',views.home),
]
