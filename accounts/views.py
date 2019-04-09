from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.views import (
    LoginView, 
)

# Create your views here.

class LogInView(LoginView):
    template_name = 'accounts/login.html'