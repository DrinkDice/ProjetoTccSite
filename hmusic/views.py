from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Instrumentos
from django.views.generic import TemplateView, ListView, DetailView


class HomePage(TemplateView):
    template_name = 'homepage.html'


class Login(TemplateView):
    template_name = 'login.html'


class Homeprodutos(ListView):
    template_name = "homeprodutos.html"
    model = Instrumentos
    #object_List


class Detalhesproduto(DetailView):
    template_name = "detalhesproduto.html"
    model = Instrumentos
    # object - > 1 item da lista de produtos sera exibido ao selecionar um produto na home page

    def get_context_data(self, **kwargs):
        context = super(Detalhesproduto, self).get_context_data(**kwargs)
        #filtrar tabela de filmes de acordo com a categoria
        self.get_object()
        produtos_relacionados = Instrumentos.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["produtos_relacionados"] = produtos_relacionados
        return context


