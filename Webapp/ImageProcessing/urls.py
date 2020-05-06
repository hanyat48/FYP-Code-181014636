from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Home', views.Home, name='Home'),
    path('twoRegistration', views.twoRegistration, name='twoRegistration'),
    path('Reconstruction', views.Reconstruction, name='Reconstruction'),
    path('Denoising', views.Denoising, name='Denoising'),
    path('Masking', views.Masking, name='Masking'),
    path('Length', views.Length, name='Length'),
    path('SuggestedDecay', views.SuggestedDecay, name='SuggestedDecay'),
]
