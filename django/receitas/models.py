from datetime import datetime
from django.db import models
from pessoas.models import Pessoa

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=50)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.nome_receita
