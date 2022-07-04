from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
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
    foto_receita = models.ImageField(upload_to='fotos-receitas/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome_receita

