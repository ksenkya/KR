from django.contrib import admin
from django.urls import path
from KR import views

urlpatterns = [
    path('', views.index),
    path('second/', views.second),
]