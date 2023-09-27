from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Instrumentos
from django.views.generic import TemplateView, ListView


class HomePage(TemplateView):
    template_name = 'homepage.html'


class Login(TemplateView):
    template_name = 'login.html'


class Homeprodutos(ListView):
    template_name = "homeprodutos.html"
    model = Instrumentos
    #object_List



