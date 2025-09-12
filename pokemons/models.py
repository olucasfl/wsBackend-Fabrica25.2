from django.db import models
from treinadores.models import Treinador

class Pokemon(models.Model):
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE, related_name="pokemons")
    nome = models.CharField(max_length=100)
    sprite = models.URLField()
    tipos = models.CharField(max_length=200)
    stats = models.JSONField()

    def __str__(self):
        return f"{self.nome} ({self.treinador.nome})"