from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('pricing/', views.pricing),
    path('contact/', views.contact),
]
