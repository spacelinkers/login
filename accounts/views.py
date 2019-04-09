from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.views import (
    LoginView, LogoutView, 
)

# Create your views here.

class HomeView(TemplateView):
    template_name = 'accounts/home.html'

class LogInView(LoginView):
    template_name = 'accounts/login.html'

class LogOutView(LogoutView):
    template_name = 'accounts/loguot.html'