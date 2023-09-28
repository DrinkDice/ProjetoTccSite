# url - view - template

from django.urls import path, include
from .views import HomePage, Login, Homeprodutos, Detalhesproduto

app_name = 'hmcontrol'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('login/', Login.as_view(), name='login'),
    path('produtos', Homeprodutos.as_view(), name='listaproduto'),
    path('produtos/<int:pk>', Detalhesproduto.as_view(), name='detalhesproduto'),
]