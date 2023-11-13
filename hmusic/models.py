from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


# criar o usuario

#cirar painel de exposição do instrumento

#criar local de compra e conversa com vendedor
LISTA_CATEGORIAS = (
    ("BATERIA", "Bateria"),
    ("CORDAS", "Cordas"),
    ("ELETRONICO","Eletronico"),
    ("METAIS","Metais"),
    ("PERCUSAO","Percusao"),
    ("SOPRO","Sopro"),
    ("TECLAS","Teclas"),
    ("ACESSORIOS", "Acessorios"),
)
#Insttrumentos
# Modelo Instrumentos
# Modelo Instrumentos
class Instrumentos(models.Model):
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE, related_name='instrumentos', null=True)
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_instrumentos')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    quantidade = models.PositiveIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(default=timezone.now)
    numero_telefone = models.CharField(max_length=15, default='5511123456789')

    def __str__(self):
        return self.titulo

# Modelo Usuario
class Usuario(AbstractUser):
    instrumentos_vistos = models.ManyToManyField(Instrumentos, blank=True, related_name='usuarios_vistos')
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)

    def __str__(self):
        return self.username


