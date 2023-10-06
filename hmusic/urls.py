# url - view - template

from django.urls import path, include
from .views import HomePage, Homeprodutos, Detalhesproduto, Pesquisar, Conta, Paginavendedor, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view


app_name = 'hmcontrol'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('produtos/', Homeprodutos.as_view(), name='listaproduto'),
    path('produtos/<int:pk>', Detalhesproduto.as_view(), name='detalhesproduto'),
    path('pesquisa/', Pesquisar.as_view(), name='pesquisa'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('conta/', Conta.as_view(), name='conta'),
    path('paginavendedor/', Paginavendedor.as_view(), name='paginavendedor'),
    path('editarperfil/', Paginaperfil.as_view, name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
]