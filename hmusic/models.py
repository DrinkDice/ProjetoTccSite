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
class Instrumentos(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_instrumentos')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    #vendedor =
    # vai ser inserido pelo usuario vendedor
    #quantidades =
    #preco =
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo # + " " + self.vendedor tem que termninar aqui


class Usuario(AbstractUser):
    instrumentos_vistos = models.ManyToManyField("Instrumentos")
