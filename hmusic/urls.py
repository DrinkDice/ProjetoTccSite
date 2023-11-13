# url - view - template

from django.urls import path, include, reverse_lazy
from .views import HomePage, Homeprodutos, Detalhesproduto, Pesquisar, Conta, Paginavendedor, Paginaperfil, Criarconta, CriarInstrumento, EditarInstrumento
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static


app_name = 'hmcontrol'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('produtos/', Homeprodutos.as_view(), name='listaproduto'),
    path('produtos/<int:pk>', Detalhesproduto.as_view(), name='detalhesproduto'),
    path('pesquisa/', Pesquisar.as_view(), name='pesquisa'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('conta/<int:pk>', Conta.as_view(), name='conta'), #coloquei a chave primaria aqui para ele direcionar as informações da conta que acessou do banco <int:pk>
    path('paginavendedor/', Paginavendedor.as_view(), name='paginavendedor'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('hmcontrol:conta')), name='mudarsenha'),
    path('criarinstrumento/', CriarInstrumento.as_view(), name='criarinstrumento'),
    path('editarinstrumento/<int:pk>/', EditarInstrumento.as_view(), name='editarinstrumento'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
