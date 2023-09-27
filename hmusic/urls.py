# url - view - template

from django.urls import path, include
from .views import HomePage, Login, Homeprodutos, Detalhesproduto


urlpatterns = [
    path('', HomePage.as_view()),
    path('login/', Login.as_view()),
    path('produtos', Homeprodutos.as_view()),
    path('produtos/<int:pk>', Detalhesproduto.as_view()),
]