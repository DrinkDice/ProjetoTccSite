from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

#cria o usuario(tbm pode ser usado para criar o instrumento tudo passa pela mesma logica aula 40
class CriarContaForm(UserCreationForm):
    email = forms.EmailField()
    cpf = forms.CharField(max_length=14, required=True, help_text="Informe seu CPF.")
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'password1', 'password2')