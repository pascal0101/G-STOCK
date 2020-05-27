
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path('acceuil/', views.index),
    path('login/', views.login),
    path('vente/', views.vente),
    path('rapport/', views.rapport)
]

