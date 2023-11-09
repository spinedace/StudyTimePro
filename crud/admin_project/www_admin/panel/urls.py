from django.contrib import admin
from django.urls import path

from django import views
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('index', views.index, name="index"),
	path('calendar', views.calendar, name="calendar"),
	path('estadisticas', views.estadisticas, name="estadisticas"),
	path('ayuda', views.ayuda, name="ayuda"),
	path('login', views.login, name="login"),	
]