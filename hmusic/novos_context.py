from .models import Instrumentos

#novas variaveis/funções são colocadas no settings(tem como juntar elas mas não fiz assim deixei separada)

def lista_instrumentos_recentes(request):
    lista_instrumentos = Instrumentos.objects.all().order_by('-data_criacao')[0:8]
    return {"lista_instrumentos_recentes": lista_instrumentos} #retorna uim dicionario com o resultado do codigo depois de vasculhar o banco


def lista_em_alta(request):
    lista_instrumentos = Instrumentos.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_em_alta": lista_instrumentos}