from django.urls import path
from django.contrib import admin
from .views import home, register, login

urlpatterns = [
	path('', home, name="home"),
	path('register/', register, name="register"),
	path('login/', login, name="login"),
]