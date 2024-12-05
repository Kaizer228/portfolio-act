from django.urls import path
from django.contrib.auth import views 
from .import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('stack/', views.stack, name='stack'),
    
]
