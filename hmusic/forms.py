from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

#cria o usuario(tbm pode ser usado para criar o instrumento tudo passa pela mesma logica aula 40

class CriarContaForm(UserCreationForm):
    email = forms.EmailField(
        help_text="Informe seu endereço de e-mail."
    )
    cpf = forms.CharField(
        max_length=14,
        required=True,
        help_text="Informe seu CPF.",
        widget=forms.TextInput(attrs={'placeholder': 'XXX.XXX.XXX-XX'}),  # Adicione um placeholder
    )

    class Meta:
        model = Usuario  # Substitua pelo seu modelo de usuário personalizado, se aplicável
        fields = ('username', 'email', 'cpf', 'password1', 'password2')
        labels = {
            'username': 'Nome de usuário',  # Exemplo de rótulo personalizado
            'password1': 'Senha',  # Exemplo de rótulo personalizado
            'password2': 'Confirmar senha',  # Exemplo de rótulo personalizado
        }

    def clean_cpf(self):
        # Adicione a lógica de validação personalizada para o campo CPF, se necessário
        cpf = self.cleaned_data.get('cpf')
        # Realize a validação do CPF aqui e retorne ou levante exceções conforme necessário
        return cpf