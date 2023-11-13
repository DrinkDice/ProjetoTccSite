# Create your views here.

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from .models import Instrumentos, Usuario
from .forms import CriarContaForm, CriarInstrumentoForm, EditarInstrumentoForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy



class HomePage(TemplateView):
    template_name = 'homepage.html'


# class Login(TemplateView):
# template_name = 'login.html'

class Paginavendedor(LoginRequiredMixin, TemplateView):
    template_name = 'paginavendedor.html'


class Conta(LoginRequiredMixin, TemplateView):
    template_name = 'conta.html'

    def get_context_data(self, **kwargs):
        # Obter o usuário logado
        usuario = self.request.user

        # Obter a lista de instrumentos criados por esse usuário, ordenados por data de criação (do mais novo ao mais antigo)
        instrumentos_criados = usuario.instrumentos.all().order_by('-data_criacao')

        # Adicionar os dados ao contexto
        context = super().get_context_data(**kwargs)
        context['usuario'] = usuario
        context['instrumentos_criados'] = instrumentos_criados

        return context



class Paginaperfil(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def get_success_url(self):
        return reverse('hmcontrol:conta', args=[self.request.user.pk])


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

    def get(self, request, *args, **kwargs):
        instrumentos = self.get_object()
        usuario = request.user

        # Verifique se o usuário está autenticado
        if request.user.is_authenticated:
            # Se estiver autenticado, incremente as visualizações
            instrumentos.visualizacoes += 1
            instrumentos.save()
            # Adicione o instrumento à lista de instrumentos_vistos
            usuario.instrumentos_vistos.add(instrumentos)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesproduto, self).get_context_data(**kwargs)
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


class EditarInstrumento(LoginRequiredMixin, UpdateView):
    template_name = 'editarinstrumento.html'
    model = Instrumentos
    form_class = EditarInstrumentoForm

    def get_queryset(self):
        # Certifique-se de que apenas o usuário autenticado pode editar seus próprios instrumentos
        return Instrumentos.objects.filter(usuario=self.request.user)

    def get_success_url(self):
        return reverse('hmcontrol:detalhesproduto', args=[self.object.id])

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
