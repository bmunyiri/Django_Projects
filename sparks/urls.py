from django.urls import path
from . import views

app_name = 'sparks'

urlpatterns = [
    path('', views.sparks, name='sparks'),    
]   
