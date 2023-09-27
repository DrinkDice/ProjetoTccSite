# url - view - template

from django.urls import path, include
from .views import HomePage, Login, Homeprodutos


urlpatterns = [
    path('', HomePage.as_view()),
    path('login/', Login.as_view()),
    path('produtos', Homeprodutos.as_view()),
]