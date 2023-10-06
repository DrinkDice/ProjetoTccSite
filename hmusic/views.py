from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Instrumentos
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(TemplateView):
    template_name = 'homepage.html'


#class Login(TemplateView):
   # template_name = 'login.html'

class Paginavendedor(LoginRequiredMixin, TemplateView):
    template_name = 'paginavendedor.html'

class Conta(LoginRequiredMixin, TemplateView):
    template_name = 'conta.html'


class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"

class Homeprodutos(ListView):
    template_name = "homeprodutos.html"
    model = Instrumentos
    #object_List


class Detalhesproduto(DetailView):
    template_name = "detalhesproduto.html"
    model = Instrumentos
    # object - > 1 item da lista de produtos sera exibido ao selecionar um produto na home page

    def get(self, request, *args, **kwargs):
        # descobrir qual o filme ele ta acessando
        instrumentos = self.get_object()
        instrumentos.visualizacoes += 1   # filme.visualizacoes + 1
        instrumentos.save()
        usuario = request.user
        usuario.instrumentos_vistos.add(instrumentos)
        # somar 1 na visualizacoes do instrumentos
        # salvar
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesproduto, self).get_context_data(**kwargs)
        #filtrar tabela de filmes de acordo com a categoria
        self.get_object()
        produtos_relacionados = Instrumentos.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["produtos_relacionados"] = produtos_relacionados
        return context

class Pesquisar(ListView):
    template_name = "pesquisar.html"
    model = Instrumentos

    #editando object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Instrumentos.objects.filter(titulo__icontains=termo_pesquisa) #Instrumentos poderia ser mudado para "self.model."
            return object_list
        else:
            return None


