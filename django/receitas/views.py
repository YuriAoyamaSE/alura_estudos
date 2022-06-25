from django.shortcuts import get_object_or_404, render
from .models import Receita

# def index(request):
#     receitas = {
#         1: 'Lasanha',
#         2: 'Sopa de legumes',
#         3: 'Sorvete',
#         4: 'Bolo de chocolate',
#         5: 'Pudim',
#         6: 'Pavê',
#     }
#     dados = {
#         'dict_receitas': receitas
#     }
#     return render(request, 'index.html', dados)


def index(request):
    receitas = Receita.objects.all()
    dados = {'receitas': receitas}
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {'receita' : receita}
    return render(request, 'receita.html', receita_a_exibir)
