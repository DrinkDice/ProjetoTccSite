# Create your views here.

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import Instrumentos, Usuario
from .forms import CriarContaForm, CriarInstrumentoForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomePage(TemplateView):
    template_name = 'homepage.html'


# class Login(TemplateView):
# template_name = 'login.html'

class Paginavendedor(LoginRequiredMixin, TemplateView):
    template_name = 'paginavendedor.html'


class Conta(LoginRequiredMixin, TemplateView):
    template_name = 'conta.html'


class Paginaperfil(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def get_success_url(self):
        return reverse('hmcontrol:conta')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('hmcontrol:login')


class Homeprodutos(ListView):
    template_name = "homeprodutos.html"
    model = Instrumentos
    # object_List


class Detalhesproduto(DetailView):
    template_name = "detalhesproduto.html"
    model = Instrumentos

    # object - > 1 item da lista de produtos sera exibido ao selecionar um produto na home page

    def get(self, request, *args, **kwargs):
        # descobrir qual o filme ele ta acessando
        instrumentos = self.get_object()
        instrumentos.visualizacoes += 1  # filme.visualizacoes + 1
        instrumentos.save()
        usuario = request.user
        usuario.instrumentos_vistos.add(instrumentos)
        # somar 1 na visualizacoes do instrumentos
        # salvar
        return super().get(request, *args, **kwargs)  # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesproduto, self).get_context_data(**kwargs)
        # filtrar tabela de filmes de acordo com a categoria
        self.get_object()
        produtos_relacionados = Instrumentos.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["produtos_relacionados"] = produtos_relacionados
        return context


def detalhes_instrumento(request, instrumento_id):
    instrumento = Instrumentos.objects.get(pk=instrumento_id)
    return render(request, 'detalhes_instrumento.html', {'instrumento': instrumento})  # teste


class CriarInstrumento(LoginRequiredMixin, FormView):
    template_name = "criarinstrumento.html"
    form_class = CriarInstrumentoForm

    def form_valid(self, form):
        if form.is_valid():
            print("O formulário é válido")
            instrumento = form.save(commit=False)
            instrumento.usuario = self.request.user
            instrumento.save()
            return super().form_valid(form)
        else:
            print("O formulário não é válido")

    def get_success_url(self):
        return reverse('hmcontrol:conta', args=[self.request.user.pk])



class Pesquisar(ListView):
    template_name = "pesquisar.html"
    model = Instrumentos

    # editando object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Instrumentos.objects.filter(
                titulo__icontains=termo_pesquisa)  # Instrumentos poderia ser mudado para "self.model."
            return object_list
        else:
            return None
