from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mission/', views.Mission, name="Mission"),
    path('vision/', views.Vision, name="Vision"),
    path('ccs/', views.CCS, name="Objectives"),
]
