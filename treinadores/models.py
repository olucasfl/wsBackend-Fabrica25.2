from django.db import models

class Treinador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=100)
    nivel = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nome} (Nível {self.nivel})"
